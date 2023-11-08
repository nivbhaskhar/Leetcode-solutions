#https://leetcode.com/problems/exclusive-time-of-functions/description/

class JobInfo:
    def __init__(self, log:str):
        split_logs = log.split(":")
        assert len(split_logs) == 3
        self.index = int(split_logs[0])
        start_or_end = split_logs[1]
        assert start_or_end in ["start", "end"]
        self.time_stamp = int(split_logs[2])
        self.is_start = start_or_end == "start"

    def __repr__(self):
        return f"job:{self.index}, is_start:{self.is_start}, time:{self.time_stamp}"
class Solution:
    def process_logs(self, logs:List[str])->List[JobInfo]:
        jobs = [JobInfo(log) for log in logs]
        return sorted(jobs, key = lambda x: x.time_stamp)
    
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        jobs = self.process_logs(logs)
        #print(f"{jobs}")

        exclusive_times = [0]*n

        processing_stack = []
        for i, job in enumerate(jobs):
            if job.is_start:
                processing_stack.append(job)
            else:
                if len(processing_stack) == 0 or processing_stack[-1].index != job.index:
                    raise ValueError(f"invalid job calls, {jobs} : pos {i}")
                job_start = processing_stack.pop()
                current_time_spent = job.time_stamp - job_start.time_stamp + 1
                exclusive_times[job.index] += current_time_spent
                if len(processing_stack) > 0:
                    prev_job = processing_stack[-1]
                    exclusive_times[prev_job.index] -= current_time_spent
        
        if len(processing_stack) > 0:
            raise ValueError(f"invalid job calls, {jobs}")
        
        return exclusive_times
