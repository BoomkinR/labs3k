using System;
using System.Collections.Generic;
using System.Runtime.Serialization;
using System.Security.Permissions;
using System.Text;
using System.Xml.Serialization;

namespace CustomSerializer
{
    [System.Xml.Serialization.XmlRootAttribute(Namespace = "", IsNullable = false)]
    [Serializable]
    public class Person : ISerializable
    {
        public Person() { }
        public Person(string name, int age, bool sex)
        {
            Name = name;
            Age = age;
            Sex = sex;
        }

        private string name;
        private bool sex;
        private int age;
        [XmlElement(ElementName ="Atribute1")]
        public string Name { get => name; set => name = value; }
        [XmlElement(ElementName = "Atribute2")]
        public bool Sex { get => sex; set => sex = value; }
        [XmlElement(ElementName = "Atribute3")]
        public int Age { get => age; set => age = value; }

        public override string ToString()
        {
            return $"class:{this.GetType()}|name:{Name}|sex:{Sex}|age:{Age}";
        }

        protected Person(SerializationInfo info, StreamingContext context)
        {
            
            Name = info.GetString("istek");
        }
        [SecurityPermissionAttribute(SecurityAction.Demand, SerializationFormatter = true)]
        public void  GetObjectData(SerializationInfo info, StreamingContext context)
        {
            info.AddValue("istek", Name);
        }
    }
}
