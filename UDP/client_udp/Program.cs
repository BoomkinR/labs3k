using System;
using System.Text;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace client_udp //CLIENT
{
    class Program
    {
        static string path = "C:\\workspace\\ftp\\ftpclienta";
        static void Main(string[] args)
        {
            Console.WriteLine("YOU ARE CLIENT");
            Thread rec = new Thread(Reciever);
            rec.Start();
            Sender(Encoding.UTF8.GetBytes("CLIENT 1 connected"));
            while (true)
            {
                var command = Console.ReadLine();
                switch (command)
                {
                    case "dir":
                        var files = Directory.GetFiles(path);
                        foreach (var item in files)
                        {
                            Console.WriteLine(Path.GetFileName(item));
                        }
                        break;
                    case "upload":
                        Console.WriteLine("Write number of sending file:");
                        string num = Console.ReadLine();
                        Sender(num);
                        break;
                        
                    default:
                        Sender(Encoding.UTF8.GetBytes(command));                                               
                        break;
                }
            }

        }

        static void Reciever()
        {
            Console.WriteLine("Client ready to recieve message");
            const string ip = "127.0.0.1";
            const int port = 9901;
            int size;
            var buffer = new byte[1024 * 950];
            IPEndPoint UdpEndPoint = new IPEndPoint(IPAddress.Parse(ip), port);
            Socket UdpSocket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
            UdpSocket.Bind(UdpEndPoint);
            EndPoint ListenerEndPoint = new IPEndPoint(IPAddress.Any, 0);
            string message;

            while (true)
            {

                    size = UdpSocket.ReceiveFrom(buffer, ref ListenerEndPoint);

                if (size < 20)
                {
                    message = Encoding.UTF8.GetString(buffer, 0, size);
                    Mg_Console(message);
                }
                else
                {
                    Console.WriteLine("Write New FileName: ");
                    string filename = Console.ReadLine();
                    BinaryWriter bWrite = new BinaryWriter(File.Open(path + "/" + filename, FileMode.Append));
                    bWrite.Write(buffer, 0, size);
                    bWrite.Close();
                }
            }
        }

        static void Sender( byte [] message)
        {
            const string ip = "127.0.0.1";
            const int port = 9900;
            const int server_port = 9910;
            int size;
            var buffer = new byte[1024 * 850];
            IPEndPoint UdpEndPoint = new IPEndPoint(IPAddress.Parse(ip), port);
            Socket UdpSocket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
            UdpSocket.Bind(UdpEndPoint);
            EndPoint SendEndPoint = new IPEndPoint(IPAddress.Parse(ip), server_port);
            

            UdpSocket.SendTo(message, SendEndPoint);


            UdpSocket.Shutdown(SocketShutdown.Both);
            UdpSocket.Close();


        }

        static void Sender(string num)
        {
            var files = Directory.GetFiles(path);
            const string ip = "127.0.0.1";
            const int port = 9900;
            const int server_port = 9910;
            int size;
            var buffer = new byte[1024 * 950];
            IPEndPoint UdpEndPoint = new IPEndPoint(IPAddress.Parse(ip), port);
            Socket UdpSocket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
            UdpSocket.Bind(UdpEndPoint);
            EndPoint SendEndPoint = new IPEndPoint(IPAddress.Parse(ip), server_port);

            buffer = File.ReadAllBytes(files[Convert.ToInt32(num)]);
            UdpSocket.SendTo(buffer, SendEndPoint);


            UdpSocket.Shutdown(SocketShutdown.Both);
            UdpSocket.Close();


        }

        static  void Mg_Console(string message)
        {
            switch (message)
            {
                case "~dir":
                    var files = Directory.GetFiles(path);
                    for (int i = 0; i < files.Length; i++)
                    {
                        Sender(Encoding.UTF8.GetBytes(Path.GetFileName(files[i]) + " --- " + i +"\n"));
                        
                    }
                    break;
                default:
                    if (Microsoft.VisualBasic.Information.IsNumeric(message))
                    {
                        Sender(message);
                    }
                    else
                    {
                        Console.WriteLine(message);
                    }
                    break;
            }

        }
    }
}