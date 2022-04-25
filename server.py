# Let's create a system receive message from an instance of my installation
# of the client.py program.
# We use the socket library to create a socket object. And use thread to thread the connection.
# We use an MariaDB client to write the data to the database.

from discord_webhook import DiscordWebhook, DiscordEmbed
import socket
import threading
import pymysql

webhook_url = "https://discord.com/api/webhooks/962749706243547136/lzWeN79baiNo6lMkiUMHjLwWuWyxfQT" \
              "-leg9Y90W_7QEdw8XPmscCpUCsGUh-cO-w1TO "


# Make a threading class for the client.
class ClientThread(threading.Thread):
    def __init__(self, client_socket, client_address):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.client_address = client_address

    def run(self):
        # While the client is connected, we will receive the message.
        ram_over_use = False
        cpu_over_use = False

        while True:

            message = self.client_socket.recv(1024)
            print(message.decode())
            # If the message is empty, we will close the connection.
            if not message:
                break

            # We will use the MariaDB client to write the data to the database.
            db = pymysql.connect(host="localhost", user="grafana", password="", database="matbeSync")
            cursor = db.cursor()
            # if messsage starts with '01:#01', we will insert the data into the mimas_ram table.
            if message.startswith('#01:01'.encode()):
                # We will split the message into the data.
                data = message.split(','.encode())
                if int(data[1].decode()) >= 85:
                    if not cpu_over_use:
                        # We will send an embed message to the discord Webhook. Create an embed object with an orange
                        # color and the title is "CPU usage warning". The description was "CPU usage is over 70%,
                        # exactly at " + data[1] + "%".
                        embed = DiscordEmbed(title="RAM usage warning", color=0xFFA500,
                                             description="RAM usage is over 85%, exactly at " + data[1].decode() + "%")
                        # Send the embed message to the discord Webhook.
                        webhook = DiscordWebhook(url=webhook_url, content="", embeds=[embed])
                        webhook.execute()
                    else:
                        pass
                elif int(data[1].decode()) >= 70:
                    if not cpu_over_use:
                        # We will send an embed message to the discord Webhook. Create an embed object with an orange
                        # color and the title is "CPU usage warning". The description was "CPU usage is over 70%,
                        # exactly at " + data[1] + "%".
                        embed = DiscordEmbed(title="RAM usage warning", color=0xFFA500, description="RAM usage is "
                                                                                                    "over 70%, "
                                                                                                    "exactly at " +
                                                                                                    data[1].decode()
                                                                                                    + "%")
                        # Send the embed message to the discord Webhook.
                        webhook = DiscordWebhook(url=webhook_url, content="", embeds=[embed])
                        webhook.execute()
                    else:
                        pass
                # We will insert the data into the database.
                try:
                    cursor.execute("INSERT INTO mimas_ram (ram) VALUES (%s)", (int(data[1].decode())))
                    db.commit()
                except Exception as e:
                    print(e)

            # if messsage starts with '#01:02', we will insert the data into the mimas_cpu table.
            if message.startswith('#01:02'.encode()):
                # We will split the message into the data.
                data = message.split(','.encode())
                if int(data[1].decode()) >= 85:
                    if not ram_over_use:
                        # We will send an embed message to the discord Webhook. Create an embed object with an orange
                        # color and the title is "CPU usage warning". The description was "CPU usage is over 70%,
                        # exactly at " + data[1] + "%".
                        embed = DiscordEmbed(title="CPU usage warning", color=0xFFA500, description="CPU usage is "
                                                                                                    "over 85%, "
                                                                                                    "exactly at " +
                                                                                                    data[1].decode()
                                                                                                    + "%")
                        # Send the embed message to the discord Webhook.
                        webhook = DiscordWebhook(url=webhook_url, content="", embeds=[embed])
                        webhook.execute()
                    else:
                        pass

                elif int(data[1].decode()) >= 70:
                    if not ram_over_use:
                        # We will send an embed message to the discord Webhook. Create an embed object with an orange
                        # color and the title is "CPU usage warning". The description was "CPU usage is over 70%,
                        # exactly at " + data[1] + "%".
                        embed = DiscordEmbed(title="CPU usage warning", color=0xFFA500, description="CPU usage is "
                                                                                                    "over 70%, "
                                                                                                    "exactly at " +
                                                                                                    data[1].decode()
                                                                                                    + "%")
                        # Send the embed message to the discord Webhook.
                        webhook = DiscordWebhook(url=webhook_url, content="", embeds=[embed])
                        webhook.execute()
                        ram_over_use = True
                    else:
                        pass

                else:
                    ram_over_use = False

                try:
                    cursor.execute("INSERT INTO mimas_cpu (cpu) VALUES (%s)", (int(data[1].decode())))
                    db.commit()
                except Exception as e:
                    print(e)

            # if messsage starts with '02:#01', we will insert the data into the paaliaq_ram table.
            if message.startswith('#02:01'.encode()):
                # We will split the message into the data.
                data = message.split(','.encode())
                if int(data[1].decode()) >= 85:
                    if not cpu_over_use:
                        # We will send an embed message to the discord Webhook. Create an embed object with an orange
                        # color and the title is "CPU usage warning". The description was "CPU usage is over 70%,
                        # exactly at " + data[1] + "%".
                        embed = DiscordEmbed(title="Paaliaq RAM usage warning", color=0xFFA500,
                                             description="RAM usage is over 85%, exactly at " + data[1].decode() + "%")
                        # Send the embed message to the discord Webhook.
                        webhook = DiscordWebhook(url=webhook_url, content="", embeds=[embed])
                        webhook.execute()
                    else:
                        pass
                elif int(data[1].decode()) >= 70:
                    if not cpu_over_use:
                        # We will send an embed message to the discord Webhook. Create an embed object with an orange
                        # color and the title is "CPU usage warning". The description was "CPU usage is over 70%,
                        # exactly at " + data[1] + "%".
                        embed = DiscordEmbed(title="Paaliaq RAM usage warning", color=0xFFA500, description="RAM "
                                                                                                            "usage is"
                                                                                                            " over "
                                                                                                            "70%, "
                                                                                                            "exactly "
                                                                                                            "at " +
                                                                                                            data[1].decode() + "%")
                        # Send the embed message to the discord Webhook.
                        webhook = DiscordWebhook(url=webhook_url, content="", embeds=[embed])
                        webhook.execute()
                    else:
                        pass
                # We will insert the data into the database.
                try:
                    cursor.execute("INSERT INTO paaliaq_ram (ram) VALUES (%s)", (int(data[1].decode())))
                    db.commit()
                except Exception as e:
                    print(e)

            # if messsage starts with '#02:02', we will insert the data into the paaliaq_cpu table.
            if message.startswith('#02:02'.encode()):
                # We will split the message into the data.
                data = message.split(','.encode())
                if int(data[1].decode()) >= 85:
                    if not ram_over_use:
                        # We will send an embed message to the discord Webhook. Create an embed object with an orange
                        # color and the title is "CPU usage warning". The description was "CPU usage is over 70%,
                        # exactly at " + data[1] + "%".
                        embed = DiscordEmbed(title="Paaliaq CPU usage warning", color=0xFFA500, description="CPU "
                                                                                                            "usage is"
                                                                                                            " over "
                                                                                                            "85%, "
                                                                                                            "exactly "
                                                                                                            "at " +
                                                                                                            data[

                                                                                                                1].decode() + "%")
                        # Send the embed message to the discord Webhook.
                        webhook = DiscordWebhook(url=webhook_url, content="", embeds=[embed])
                        webhook.execute()
                    else:
                        pass

                elif int(data[1].decode()) >= 70:
                    if not ram_over_use:
                        # We will send an embed message to the discord Webhook.
                        # Create an embed object with an orange color and the title is "CPU usage warning". The description was "CPU usage is over 70%, exactly at " + data[1] + "%".
                        embed = DiscordEmbed(title="Paaliaq CPU usage warning", color=0xFFA500, description="CPU usage is over 70%, exactly at " + data[1].decode() + "%")
                        # Send the embed message to the discord Webhook.
                        webhook = DiscordWebhook(url=webhook_url, content="", embeds=[embed])
                        webhook.execute()
                        ram_over_use = True
                    else:
                        pass

                else:
                    ram_over_use = False

                try:
                    cursor.execute("INSERT INTO paaliaq_cpu (cpu) VALUES (%s)", (int(data[1].decode())))
                    db.commit()
                except Exception as e:
                    print(e)


# Create a socket object
s = socket.socket()
# Bind to the port
port = 52365
s.bind(('0.0.0.0', port))

# make loop to listen for connections
while True:
    s.listen(5)
    # accept connection
    c, addr = s.accept()

    # create a thread for the client
    client_thread = ClientThread(c, addr)
    client_thread.start()
    print("Got connection from", addr)
