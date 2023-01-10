import operator

ops = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul}


class Monkey:
    def __init__(self, name, job) -> None:
        self.name = name
        self.job = job

    def yell(self):
        job_list = self.job.split()
        if len(job_list) == 1:
            return int(job_list[0])
        elif len(job_list) == 3:
            if job_list[0].isnumeric() and job_list[2].isnumeric():
                return ops[job_list[1]](int(job_list[0]), int(job_list[2]))
            elif job_list[0].isnumeric():
                return f"Waiting for monkey: {job_list[2]}"
            elif job_list[2].isnumeric():
                return f"Waiting for monkey: {job_list[0]}"
            else:
                return job_list[0].yell()

    def operator(self):
        job_list = self.job.split()
        if len(job_list) == 3:
            return job_list[1]
