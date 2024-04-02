import time

def execution_time_logger(func):

    def wrapper (*args, **kwargs):

        start_time= time.time()

        result= func(*args, **kwargs)

        end_time = time.time()

        print(f"Execution time: {end_time-start_time}seconds")
        return result

    return wrapper


class TransactionalBlock:

    def __enter__(self):

        print ("Transaction started")
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type:

            print("Transaction rolled back")

            raise exc_val

        else:

            print ("Transaction committed")


@execution_time_logger

def run_transaction ():

    with TransactionalBlock():

        print ("Performing transaction")

        # Simulate a transaction operation and error condition

        # Uncomment the next line to simulate an exception

        #raise Exception ("We need this exception here!")

run_transaction()