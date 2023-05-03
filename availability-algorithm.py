import time

last_update = time.time()

while True:
    # Check time elapsed since last update
    elapsed_time = time.time() - last_update
    if elapsed_time > 60:
        print('Alert: Input fields have not been updated in over 1 minute.')
        # You can add code here to send an alert message or take other actions as needed
    
    # Get new input from user
    workers = int(input('Number of workers: '))
    clients = int(input('Number of clients: '))
    last_update = time.time()
    
    # Check service availability based on inputs
    if workers >= clients:
        print('Service is on its way')
    else:
        print('Service is unavailable due to high demand. We are working to scale our services. Thank you for your understanding.')
    
    # Wait for 30 seconds before checking again
    time.sleep(30)
