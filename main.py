def main():
    # how the demo will go
    print("start demo")
    print("create person A")
    print("create person B")
    print("create person C")
    print("create person D")
    print("create person E")
    print("person A create group with B, C, D")
    print("person B,C,D accept group invite")
    print("person A create a meeting entry with group")
    print("person B,C,D accept meeting invite")

    print("person E create group with D")
    print("person D accept group invite")
    print("person E try to create a meeting entry with group that happen to conflict with person A's meeting")
    print("person E see that person D is not free at that time")
    print("person E change the meeting entry time")
    print("person D accept meeting invite")

    print("end demo")
    return


if __name__ == '__main__':
    main()
