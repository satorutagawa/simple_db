import sys
from collections import defaultdict

class database():
    def __init__(self):
        self.data = dict()
        self.val_count = defaultdict(int)
        self.transactions = []
        self.transaction_idx = -1

    def run_command(self, cmd_str: str):
        if self.transaction_idx==-1:
            cmd = cmd_str.split()[0]
            if cmd == 'SET':
                self.set(cmd_str.split()[1], int(cmd_str.split()[2]))
            elif cmd == 'GET':
                return self.get(cmd_str.split()[1])
            elif cmd == 'DELETE':
                return self.delete(cmd_str.split()[1])
            elif cmd == 'COUNT':
                return self.count(int(cmd_str.split()[1]))
            else:
                sys.stderr.write(f"Invalid cmd={cmd}")
                sys.exit(1)
        else:
            print(self.transaction_idx)
            self.transactions[self.transaction_idx].append(cmd_str)

    def set(self, name: str, value: int):
        if name in self.data:
            tmp_val = self.data[name]
            self.val_count[tmp_val] -= 1

        self.data[name] = value
        self.val_count[value] += 1

    def get(self, name: str) -> str:
        if name in self.data:
            return self.data[name]
        else:
            return "NULL"

    def delete(self, name: str):
        if name in self.data:
            val = self.data[name]
            del self.data[name]
            self.val_count[val] -= 1

    def count(self, value: int):
        return self.val_count[value]

    def begin(self):
        self.transaction_idx += 1
        # []
        self.transactions.append([])
        # [[]]

    def rollback(self):
        self.transactions.pop(self.transaction_idx)
        self.transaction_idx -= 1

    def commit(self):
        if self.transaction_idx == -1:
            return

        # run commands from beginning
        for i in range(len(self.transaction_idx)):
            print(i)
            for cmd in self.transactions[i]:
                print(cmd)
                #self.run_command(cmd)
