using System;
using System.Collections.Generic;
using System.Text;
using System.Runtime.Serialization;
using System.IO;
using System.Reflection;
using System.Linq;


namespace CustomSerializer
{
    class CustomSerializer: IFormatter
    {
        Type type;

        public SerializationBinder Binder { get; set; }
        public StreamingContext Context { get; set; }
        public ISurrogateSelector SurrogateSelector { get; set; }

        public CustomSerializer( Type _type)
        {
            this.type = _type;
        }

        public void ToSerializeObject(object obj, string Filepath, string format)
        {
            StreamWriter streamWriter = new StreamWriter(Filepath);
            List<PropertyInfo> list = type.GetProperties().ToList();
            string mas = obj.GetType().ToString() ;
            foreach (var item in list)
            {
                mas += $"|{item.Name}:{item.GetValue(obj)}";
            }
            

        }

        public void CBinarySerializer(string obj, string Filepath)
        {
            //byte[] byte = Encoding.UTF8.GetBytes(obj);

        }
        public object CBinaryDeserializer(string Filepath)
        {
            return 0;
        }

        public void CXMLSerializer(Type datatype, object obj, string Filepath)
        {


        }

        public object CXMLDeserializer(Type datatype, string Filepath)
        {

            return 0;
        }

        public void CJsonSerialize(object obj, string Filepath)
        {

        }

        public Object CJsonDeserialize(Type datatype, string Filepath)
        {
            return 0;

        }

        public object Deserialize(Stream serializationStream)
        {
            throw new NotImplementedException();
        }

        public void Serialize(Stream serializationStream, object graph)
        {
            throw new NotImplementedException();
        }
    }
}
