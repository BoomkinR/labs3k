using System;
using System.Collections.Generic;
using System.Text;

namespace SerJohn
{
    class Person
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

        public string Name { get => name; set => name = value; }
        public bool Sex { get => sex; set => sex = value; }
        public int Age { get => age; set => age = value; }
    }
}
