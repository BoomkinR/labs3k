using System;
using System.Collections;
using System.Collections.Generic;
using System.Xml.Serialization;
using System.IO;
using SerJohn;
using System.Security;
using System.Text.Json;
using System.Text.Json.Serialization;

[assembly: AllowPartiallyTrustedCallers]
namespace PersonClass
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Person> book = new List<Person>();
            string a = "";
            var path = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
            while (a != "end")
            {
                Console.WriteLine("WHAT TO DO: ");
                a = Console.ReadLine();
                switch (a)
                {
                    case "new":
                        Console.WriteLine("Write name: ");
                        string name = Console.ReadLine();
                        Console.WriteLine("Write age: ");
                        int age = Convert.ToInt32(Console.ReadLine());
                        Console.WriteLine("1-male 2-female");
                        bool sex = Convert.ToBoolean(Console.ReadLine());
                        book.Add(new Person(name, age, sex));
                        Console.ReadLine();
                        break;
                    case "write":
                        
                        SerJohn.Serializer serialiser = new SerJohn.Serializer();
                        serialiser.BinarySerializer(book , path + "//Serial.save");
                        serialiser.XMLSerializer(typeof(List<Person>), book, path + "//Serial.xml");
                        serialiser.JsonSerialize(book, path + "//Serial.json");
                        Console.WriteLine("DONE");
                       
                   
                        break;

                    case "read":
                        Console.WriteLine("######################/SPAWNING_PERSONAL/###############################");
                       

                        Serializer serializer = new Serializer();
                        
                        book = serializer.BinaryDeserializer(path + "//Serial.save") as List<Person>;
                        Console.WriteLine("FROM BINARY");
                        foreach (var item in book)
                        {
                            Console.WriteLine(item.Name);
                        }

                        book = serializer.XMLDeserializer(typeof(List<Person>), path + "//Serial.xml") as List<Person>;
                        Console.WriteLine("FROM XML");
                        foreach (var item in book)
                        {
                            Console.WriteLine(item.Name);
                        }

                   //     book = serializer.JsonDeserialize(typeof(List<Person>), path + "//Serial.json") as List<Person>;
                        string jsonString = File.ReadAllText(path + "//Serial.json");
                        object obj = JsonSerializer.Deserialize<List<Person>>(jsonString);
                        Console.WriteLine("FROM JSON");
                        foreach (var item in book)
                        {
                            Console.WriteLine(item.Name);
                        }
                        break;
                    default:
                        break;
                }
            }
        }
    }
}
