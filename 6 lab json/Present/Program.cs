using System;
using System.Xml.Serialization;
using System.IO;
using System.Collections.Generic;
using SerJohn;
using System.Security;
using System.Text.Json;
using System.Text.Json.Serialization;


[assembly: AllowPartiallyTrustedCallers]
namespace Present
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("######################/SPAWNING_PERSONAL/###############################");
            var path = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments) ;

            Serializer serializer = new Serializer();
            List<Person> book;
            //book = serializer.BinaryDeserializer(path + "//Serial.save") as List<Person>;
            //Console.WriteLine("FROM BINARY");
            //foreach (var item in book)
            //{
            //    Console.WriteLine(item.Name);
            //}

            book = serializer.XMLDeserializer(typeof(List<Person>), path + "//Serial.xml") as List<Person>;
            Console.WriteLine("FROM XML");
            foreach (var item in book)
            {
                Console.WriteLine(item.Name);
            }

            //      book = serializer.JsonDeserialize(typeof(List<Person>), path + "//Serial.json") as List<Person>;
            string jsonString = File.ReadAllText(path + "//Serial.json");
            object obj = JsonSerializer.Deserialize<List<Person>>(jsonString);
            Console.WriteLine("FROM JSON");
            Console.WriteLine("FROM JSON");
            foreach (var item in book)
            {
                Console.WriteLine(item.Name);
            }
            Console.ReadKey();



        }
    }
}
