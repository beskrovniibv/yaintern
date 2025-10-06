#! /usr/bin/env python

# J. Листы и вью*

# https://contest.yandex.ru/contest/80939/problems/J/

n = int(input())
lists = {}
sublists = {}
for _ in range(n):
    cmdline = input()
    cmd_parse = cmdline.split()
    if cmd_parse[0] == 'List':
        list_name = cmd_parse[1]
        if cmd_parse[3] == "new":  # create new list
            values = cmd_parse[-1]
            values = values.lstrip("List(").rstrip(")").split(",")
            lists[list_name] = ["*"] + values
            # print(f"create new list {list_name} with values {values}")
        else:  # create new sublist
            values = cmd_parse[-1].split(".")
            sublist_name = list_name
            list_name = values[0]
            values = values[1]
            values = list(map(int, values.lstrip("subList(").rstrip(")").split(",")))
            if list_name in lists:
                sublists[sublist_name] = (list_name, values)
            else:
                t = list_name
                list_name = sublists[list_name][0]
                values = [sublists[t][1][0] + values[0] - 1, sublists[t][1][0] + values[1] - 1]
                sublists[sublist_name] = (list_name, values)
            # print(f"create sublist {sublist_name} from list {list_name} with values {values}")
    else:
        cmd_parse = cmd_parse[0].split(".")
        list_name = cmd_parse[0]
        cmd = cmd_parse[1][:3]
        args = list(map(int, cmd_parse[1].lstrip("set(").lstrip("add(").lstrip("get(").rstrip(")").split(",")))
        if cmd == "set":
            idx = args[0]
            if list_name in sublists:
                idx = sublists[list_name][1][0] + idx - 1
                list_name = sublists[list_name][0]
            lists[list_name][idx] = args[1]
        elif cmd == "add":
            lists[list_name].append(args[0])
        elif cmd == "get":
            idx = args[0]
            if list_name in sublists:
                idx = sublists[list_name][1][0] + idx - 1
                list_name = sublists[list_name][0]
            print(lists[list_name][idx])
        # print(f"{cmd} at {list_name} with {args}")
    # print(cmd_parse)
