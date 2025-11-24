def tuple_operation():

    t = (1,2,3,4,5,6)

    while True:
        print("\n1.Count")
        print("2.Index")
        print("3.Length")
        print("4.Max")
        print("5.Min")
        print("6.Exit")
        choice = input("Enter choice:")

        if choice == '1':
            print("2 appears", t.count(2),"times")
