namespace DerriksForgeTools
{
    partial class DevForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.button_gatherItemData = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // button_gatherItemData
            // 
            this.button_gatherItemData.Location = new System.Drawing.Point(12, 12);
            this.button_gatherItemData.Name = "button_gatherItemData";
            this.button_gatherItemData.Size = new System.Drawing.Size(114, 35);
            this.button_gatherItemData.TabIndex = 0;
            this.button_gatherItemData.Text = "Gather Item Data";
            this.button_gatherItemData.UseVisualStyleBackColor = true;
            this.button_gatherItemData.Click += new System.EventHandler(this.button_gatherItemData_Click);
            // 
            // DevForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.button_gatherItemData);
            this.Name = "DevForm";
            this.Text = "DevForm";
            this.ResumeLayout(false);

        }

        #endregion

        private Button button_gatherItemData;
    }
}