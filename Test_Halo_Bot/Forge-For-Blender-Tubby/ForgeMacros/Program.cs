// See https://aka.ms/new-console-template for more information


using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
using System.Drawing;
using Tesseract;
using WindowsInput;
using WindowsInput.Native;
using System.Drawing;
using System.Drawing.Imaging;
using System.Text;
using System.Windows.Forms;
using ForgeMacros;
using ImageFormat = System.Drawing.Imaging.ImageFormat;


//sim.Keyboard.KeyDown(VirtualKeyCode.VK_R);
//maybe sleep or something?
//sim.Keyboard.KeyUp(VirtualKeyCode.VK_R);
//or just use the whole press
//sim.Keyboard.KeyPress(VirtualKeyCode.VK_R);

//sim.Mouse.MoveMouseTo(0, 0);
//sim.Mouse.LeftButtonClick();
NativeHelper.CallBackPtr callBackPtr = new NativeHelper.CallBackPtr(WriteWindow);


var stringBuilder = new StringBuilder(256);
var s = NativeHelper.GetClassName(NativeHelper.GetForegroundWindow(), stringBuilder, stringBuilder.Capacity);
var st = stringBuilder.ToString();

//NativeHelper.SetActiveWindow()

Console.WriteLine(st);
NativeHelper.EnumWindows(callBackPtr, 0);

static bool WriteWindow(int hwnd, int lPram)
{
    var stringBuilder = new StringBuilder(256);
    var i = NativeHelper.GetClassName((IntPtr)hwnd, stringBuilder, stringBuilder.Capacity);

    if (i != 0)
    {
        var s = stringBuilder.ToString();
        if (s.Contains("Halo"))
        {
            Console.WriteLine(s);
            NativeHelper.SetForegroundWindow((IntPtr)hwnd);
            Thread.Sleep(100);
            Input.Simulate.Keyboard.KeyPress(VirtualKeyCode.VK_R);
        }
    }

    return true;
}