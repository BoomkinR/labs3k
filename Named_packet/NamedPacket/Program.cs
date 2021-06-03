using System;
using System.IO;
using System.IO.Pipes;
using System.Text;
using System.Threading;

public class PipeServer
{
    private static int numThreads = 4;

    public static void Main()
    {
        var buffer = new byte[1024 * 128];

        string message;


        Console.WriteLine("\n*** Named pipe server stream with impersonation example ***\n");
        Console.WriteLine("Waiting for client connect...\n");
        NamedPipeServerStream pipeServer =
        new NamedPipeServerStream("testpipe", PipeDirection.InOut, numThreads);
        var files = Directory.GetFiles("C:\\WORKSPACE\\Named_packet\\serv");

        pipeServer.WaitForConnection();
        while (true)
        {


            var size = pipeServer.Read(buffer);
            message = Encoding.UTF8.GetString(buffer, 0 , size);
            if (message == "download")
            {
                var stroka = "";
                for (int i = 0; i < files.Length; i++)
                {
                    stroka += Path.GetFileName(files[i]) + " - " + i +"\n";
                }
                pipeServer.Write(Encoding.UTF8.GetBytes(stroka));

                size = pipeServer.Read(buffer);
                message = Encoding.UTF8.GetString(buffer,0,size);
                var path = files[Convert.ToInt32(message)];
                buffer = File.ReadAllBytes(path);
                pipeServer.Write(buffer);

            }
            else if (message == "upload")
            {
                Console.WriteLine("Client trying to give u file. Choose a name:::");
                var name = Console.ReadLine();
                size = pipeServer.Read(buffer);
                File.WriteAllBytes("C:\\WORKSPACE\\Named_packet\\serv\\" + name, buffer);
            }
            else
            {
                Console.WriteLine(message);
            }

        }
        Console.ReadKey();
        pipeServer.Close();
    }

}

// Defines the data protocol for reading and writing strings on our stream
public class StreamString
{
    private Stream ioStream;
    private UnicodeEncoding streamEncoding;

    public StreamString(Stream ioStream)
    {
        this.ioStream = ioStream;
        streamEncoding = new UnicodeEncoding();
    }

    public string ReadString()
    {
        int len = 0;

        len = ioStream.ReadByte() * 256;
        len += ioStream.ReadByte();
        byte[] inBuffer = new byte[len];
        ioStream.Read(inBuffer, 0, len);

        return streamEncoding.GetString(inBuffer);
    }

    public int WriteString(string outString)
    {
        byte[] outBuffer = streamEncoding.GetBytes(outString);
        int len = outBuffer.Length;
        if (len > UInt16.MaxValue)
        {
            len = (int)UInt16.MaxValue;
        }
        ioStream.WriteByte((byte)(len / 256));
        ioStream.WriteByte((byte)(len & 255));
        ioStream.Write(outBuffer, 0, len);
        ioStream.Flush();

        return outBuffer.Length + 2;
    }
}

// Contains the method executed in the context of the impersonated user
public class ReadFileToStream
{
    private string fn;
    private StreamString ss;

    public ReadFileToStream(StreamString str, string filename)
    {
        fn = filename;
        ss = str;
    }

    public void Start()
    {
        string contents = File.ReadAllText(fn);
        ss.WriteString(contents);
    }
}