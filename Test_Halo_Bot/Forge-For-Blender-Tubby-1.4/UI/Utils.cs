using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DerriksForgeTools
{
    public static class Utils
    {

        public static bool SelectFolderDialog(out string selectedPath)
        {
            FolderBrowserDialog fileDialog = new FolderBrowserDialog();



            if (fileDialog.ShowDialog() == DialogResult.OK)
            {
                selectedPath = fileDialog.SelectedPath;
                return true;
            }

            selectedPath = "";
            return false;
        }


    }
}
