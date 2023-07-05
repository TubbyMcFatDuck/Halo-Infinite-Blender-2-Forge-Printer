namespace DerriksForgeTools;

partial class Form1
{
    /// <summary>
    ///  Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    ///  Clean up any resources being used.
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
    ///  Required method for Designer support - do not modify
    ///  the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
            this.button_LoadBlenderJson = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.textBox_MvarName = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label_ExportPath = new System.Windows.Forms.Label();
            this.button2 = new System.Windows.Forms.Button();
            this.button_dev = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // button_LoadBlenderJson
            // 
            this.button_LoadBlenderJson.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(68)))), ((int)(((byte)(71)))), ((int)(((byte)(90)))));
            this.button_LoadBlenderJson.FlatAppearance.BorderSize = 0;
            this.button_LoadBlenderJson.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.button_LoadBlenderJson.Font = new System.Drawing.Font("Segoe UI", 16F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.button_LoadBlenderJson.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(248)))), ((int)(((byte)(248)))), ((int)(((byte)(242)))));
            this.button_LoadBlenderJson.Location = new System.Drawing.Point(12, 8);
            this.button_LoadBlenderJson.Name = "button_LoadBlenderJson";
            this.button_LoadBlenderJson.Size = new System.Drawing.Size(276, 53);
            this.button_LoadBlenderJson.TabIndex = 6;
            this.button_LoadBlenderJson.Text = "Create mvar";
            this.button_LoadBlenderJson.UseVisualStyleBackColor = false;
            this.button_LoadBlenderJson.Click += new System.EventHandler(this.button_LoadBlenderJson_Click);
            // 
            // button1
            // 
            this.button1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(68)))), ((int)(((byte)(71)))), ((int)(((byte)(90)))));
            this.button1.FlatAppearance.BorderSize = 0;
            this.button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.button1.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.button1.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(248)))), ((int)(((byte)(248)))), ((int)(((byte)(242)))));
            this.button1.Location = new System.Drawing.Point(294, 8);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(84, 53);
            this.button1.TabIndex = 7;
            this.button1.Text = "Set Save Location";
            this.button1.UseVisualStyleBackColor = false;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // textBox_MvarName
            // 
            this.textBox_MvarName.Location = new System.Drawing.Point(89, 67);
            this.textBox_MvarName.Name = "textBox_MvarName";
            this.textBox_MvarName.Size = new System.Drawing.Size(100, 23);
            this.textBox_MvarName.TabIndex = 8;
            this.textBox_MvarName.TextChanged += new System.EventHandler(this.textBox_MvarName_TextChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.label1.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(248)))), ((int)(((byte)(248)))), ((int)(((byte)(242)))));
            this.label1.Location = new System.Drawing.Point(10, 70);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(73, 15);
            this.label1.TabIndex = 9;
            this.label1.Text = "mvar name:";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // label_ExportPath
            // 
            this.label_ExportPath.AutoSize = true;
            this.label_ExportPath.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.label_ExportPath.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(248)))), ((int)(((byte)(248)))), ((int)(((byte)(242)))));
            this.label_ExportPath.Location = new System.Drawing.Point(12, 99);
            this.label_ExportPath.Name = "label_ExportPath";
            this.label_ExportPath.Size = new System.Drawing.Size(192, 15);
            this.label_ExportPath.TabIndex = 10;
            this.label_ExportPath.Text = "C://test/test/test/test/Text.mvar";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(8, 117);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 11;
            this.button2.Text = "About";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click_1);
            // 
            // button_dev
            // 
            this.button_dev.Location = new System.Drawing.Point(303, 110);
            this.button_dev.Name = "button_dev";
            this.button_dev.Size = new System.Drawing.Size(75, 23);
            this.button_dev.TabIndex = 12;
            this.button_dev.Text = "Dev";
            this.button_dev.UseVisualStyleBackColor = true;
            this.button_dev.Click += new System.EventHandler(this.button_dev_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(40)))), ((int)(((byte)(42)))), ((int)(((byte)(54)))));
            this.ClientSize = new System.Drawing.Size(390, 145);
            this.Controls.Add(this.button_dev);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.label_ExportPath);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.textBox_MvarName);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.button_LoadBlenderJson);
            this.Name = "Form1";
            this.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.Text = "Blender To Forge Converter";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

    }

    #endregion

    private OpenFileDialog openFileDialog1;
    private Button button_LoadBlenderJson;
    private Button button1;
    private TextBox textBox_MvarName;
    private Label label1;
    private Label label_ExportPath;
    private Button button2;
    private Button button_dev;
}