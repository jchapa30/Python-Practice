def main():
    # String (str)
    instance_type = "t2.micro"
    message = "My instances are of type:"

    # Integer (int)
    num_of_instances = 5
    hours_running = 10

    # Floating-point numbers (float)
    average_load = 2.5
    total_cost = 42.75

    # Boolean
    is_running = True
    is_stopped = False

    print(f'{message} {instance_type}. I have {num_of_instances} of them and they have been running {hours_running} hours.')
    print(f'The average load is {average_load} and the total cost is ${total_cost:.2f}.')
    print(f'Is the instance running? {is_running}')
    print(f'Is the instance stopped? {is_stopped}')

if __name__ == '__main__':
    main()





