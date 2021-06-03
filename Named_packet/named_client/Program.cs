using System;
using System.Diagnostics;
using System.IO;
using System.IO.Pipes;
using System.Security.Principal;
using System.Text;
using System.Threading;

public class PipeClient
{
    private static int numClients = 4;

    public static void Main(string[] args)
    {
        var buffer = new byte[1024 * 128];
        var pipeClient =
                     new NamedPipeClientStream(".", "testpipe",
                         PipeDirection.InOut, PipeOptions.None,
                         TokenImpersonationLevel.Impersonation);
        pipeClient.Connect();
        Console.WriteLine("Write 'download' or 'upload'");
        var command = Console.ReadLine();
        pipeClient.Write(Encoding.UTF8.GetBytes(command));
        while (true)
        {
            if (command == "download")
            {
                var size = pipeClient.Read(buffer);
                Console.WriteLine(Encoding.UTF8.GetString(buffer , 0 , size));
                Console.WriteLine("Write a num of file:::");
                pipeClient.Write(Encoding.UTF8.GetBytes(Console.ReadLine()));
                Console.WriteLine("Write a name of file");
                var name = Console.ReadLine();
                 size = pipeClient.Read(buffer);
                File.WriteAllBytes("C:\\WORKSPACE\\Named_packet\\cli\\" + name, buffer);
            }
            else if (command == "upload")
            {
                var files = Directory.GetFiles("C:\\WORKSPACE\\Named_packet\\cli");

                for (int i = 0; i < files.Length; i++)
                {
                    Console.WriteLine(Path.GetFileName(files[i]) + " - " + i);
                }
                Console.WriteLine("Write a num of file");
                int num = Convert.ToInt32(Console.Read());
                var path = files[num];
                buffer = File.ReadAllBytes(path);
                pipeClient.Write(buffer);

            }

        }
        Console.ReadKey();
        pipeClient.Close();
    }

}