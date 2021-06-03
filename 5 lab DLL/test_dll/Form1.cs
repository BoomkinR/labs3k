using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using LiveCharts;
using LiveCharts.Charts;
using LiveCharts.Wpf;

namespace test_dll
{
    public partial class Form1 : Form
    {
        [DllImport(@"C:\WORKSPACE\5 lab DLL\DTime\Debug\Dtime.dll", CallingConvention = CallingConvention.Cdecl)]
        public static extern int Hour();
        [DllImport(@"C:\WORKSPACE\5 lab DLL\DTime\Debug\Dtime.dll", CallingConvention = CallingConvention.Cdecl)]
        public static extern int Minute();
        [DllImport(@"C:\WORKSPACE\5 lab DLL\DTime\Debug\Dtime.dll", CallingConvention = CallingConvention.Cdecl)]
        public static extern int Second();
        SeriesCollection series = new SeriesCollection();
        ChartValues<int> values = new ChartValues<int>();
        List<string> time = new List<string>();
        public Form1()
        {
            InitializeComponent();
            
        }

        private void toolStripButton1_Click(object sender, EventArgs e)
        {
            var ran = new Random();
            values.Add(ran.Next(0, 100));
            time.Add($"{Hour()}:{Minute()}:{Second()}");
            cartesianChart1.AxisX.Clear();
            cartesianChart1.AxisX.Add(new Axis()
            {
                Title = "TIME",
                Labels = time
            });
            LineSeries Line = new LineSeries();
            Line.Title = "user1";
            Line.Values = values;
            series.Clear();
            series.Add(Line);
            cartesianChart1.Series = series;
        }
    }
}
