using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Threading.Tasks;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.Xml.Serialization;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Security;


[assembly: AllowPartiallyTrustedCallers]
namespace SerJohn
{
    public class Serializer
    {

        public void BinarySerializer(object obj, string Filepath)
        {
            FileStream file;
            BinaryFormatter writer = new BinaryFormatter();
            if (File.Exists(Filepath)) File.Delete(Filepath);
            file = File.Create(Filepath);
            writer.Serialize(file, obj);
            file.Close();
        }
        public object BinaryDeserializer(string Filepath)
        {
            FileStream file;
            object obj = null;
            BinaryFormatter writer = new BinaryFormatter();
            if (File.Exists(Filepath))
            {
                file = File.OpenRead(Filepath);
                obj = writer.Deserialize(file);
                file.Close();
            }
            return obj;
        }

        public void XMLSerializer(Type datatype, object obj, string Filepath)
        {
            XmlSerializer writer = new XmlSerializer(datatype);
            FileStream file;
            if (File.Exists(Filepath)) File.Delete(Filepath);
            file = File.Create(Filepath);
            writer.Serialize(file, obj);
            file.Close();

        }

        public object XMLDeserializer(Type datatype, string Filepath)
        {
            object obj = null;
            FileStream file;
            XmlSerializer writer = new XmlSerializer(datatype);
            if (File.Exists(Filepath))
            {
                file = File.OpenRead(Filepath);
                obj = writer.Deserialize(file);
                file.Close();
            }
            return obj;
        }

        public void JsonSerialize(object obj, string Filepath)
        {
            string jsonString = JsonSerializer.Serialize(obj);
            File.WriteAllText(Filepath, jsonString);
        }

        public Object JsonDeserialize(Type datatype, string Filepath)
        {
            string jsonString = File.ReadAllText(Filepath);
            object obj = JsonSerializer.Deserialize<List<Person>>(jsonString);

            
            return obj;
            
        }


    }


}
