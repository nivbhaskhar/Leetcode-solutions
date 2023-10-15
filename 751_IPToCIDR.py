#https://leetcode.com/problems/ip-to-cidr/description/

class Solution:
    def pad_bin(self, binary: str, n: int)->str:
        """
        Given a binary string of <= n bits, pad it to its left with 0s and
        return a binary string with n bits
        """
        m = len(binary)
        if m > n:
            raise ValueError(f"invalid binary {binary} of more than {n} bits")
        else:
            return "".join(['0']*(n-m)) + binary

    def ip_to_bin(self, ip:str)->str:
        components = ip.split('.')
        if len(components) != 4:
            raise ValueError(f"invalid ip {ip}")
        binary_components = [self.get_bin(int(component), 8) for component in components]
        return "".join(binary_components)


    def bin_to_ip(self, binary: str)->str:
        if len(binary) != 32:
            raise ValueError(f"invalid binary {binary} of length {len(binary)}")
        components = []
        component = []
        for i in range(len(binary)):
            component.append(binary[i])
            if i % 8 == 7:
                temp = ''.join(component)
                assert len(temp) == 8, f"invalid component {component}"
                components.append(str(self.get_int(temp)))
                component = []
        return ".".join(components)
    
    def get_int(self, binary:str)->int:
        return int(binary,2)
    
    def get_bin(self, num: int, padding: int=32)->str:
        return self.pad_bin(bin(num)[2:], padding)

    def first_differing_bit_pos(self, start_bin: str, end_bin: str)->Optional[int]:

        assert len(start_bin) == 32 , f"binary {start_bin} has num bits = {len(start_bin)}"
        assert len(end_bin)==32, f"binary {end_bin} has num bits = {len(end_bin)}"
        for i in range(32):
            if start_bin[i] != end_bin[i]:
                assert start_bin[i] == "0", f"invalid: {start_bin} not less than {end_bin}" 
                return i
        else:
            return None

    def least_set_bit(self, binary:str)->Optional[int]:
        n = len(binary)
        assert n==32, f"binary {binary} has num bits = {len(binary)}"
        for i in range(31,-1,-1):
            if binary[i] == "1":
                return i
        else:
            return None
    
    def bin_to_cdr(self, start_bin:str, start_int: int, end_bin: str, end_int: int)->list[tuple[str, int]]:
        if start_int > end_int:
            return []
        elif start_int == end_int:
            return [(start_bin, 32)]
        elif start_int == end_int -1:
            if start_int % 2 == 0:
                return [(start_bin, 31)]
            else:
                return [(end_bin, 32), (start_bin, 32)]
        else:
            print(f"here dff > 2 {start_int}, {end_int}")
            p = self.first_differing_bit_pos(start_bin, end_bin)
            if p is None:
                raise ValueError(f"invalid case handling : {start_bin} = {end_bin}")
            lsb = self.least_set_bit(start_bin)
            if lsb is None:
                lsb = p

            if lsb > p:
                num_zeros = 31-lsb
            else:
                for i in range(31,p-1,-1):
                    if end_bin[i] == "0":
                        num_zeros = 31-p
                        break
                else:
                    num_zeros = 31-p+1

            increment = 2**(num_zeros)
            extension = (start_bin, 32-num_zeros)
            
            ans =  self.bin_to_cdr(self.get_bin(start_int+increment), start_int+increment, end_bin, end_int)
            ans.append(extension)
            return ans

                 





    def ipToCIDR(self, ip: str, n: int) -> list[str]:
        start_bin = self.ip_to_bin(ip)
        start_int = self.get_int(start_bin)
        end_int = start_int + n-1
        end_bin = self.get_bin(end_int)
        binaries_and_prefix_lengths = self.bin_to_cdr(start_bin, start_int, end_bin, end_int)
        binaries_and_prefix_lengths.reverse()
        return [f"{self.bin_to_ip(binary)}/{prefix}" for (binary, prefix) in binaries_and_prefix_lengths]