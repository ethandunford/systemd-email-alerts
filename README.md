# Systemd and Python

Running python files with Systemd.

## example.service
This service activates a virtual enviroment, imports database configuration file and runs a python script.

## How to run this service

1. Change the file paths to match your directory 
2. Copy example.service to the services folder /etc/systemd/system/
3. Enable the service sudo systemctl enable example.service
4. Start the service sudo systemctl start example.service
5. Check if service is working sudo systemctl status example.service
6. View journal log journalctl	-u example.service -f


## Useful material 

*[Digital Ocean - systemd essentials](https://www.digitalocean.com/community/tutorials/systemd-essentials-working-with-services-units-and-the-journal)
*[Digital Ocean - how to use systemctl](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)
*[loggly - usingjournalctl](https://www.loggly.com/ultimate-guide/using-journalctl/)