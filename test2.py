
import wx

class FillUpForm(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Fill Up Form')
        panel = wx.Panel(self)

        # Create input fields
        self.name_label = wx.StaticText(panel, label='Employee Name:')
        self.name_text = wx.TextCtrl(panel)
        
        self.age_label = wx.StaticText(panel, label='Age:')
        self.age_text = wx.TextCtrl(panel)
        
        self.email_label = wx.StaticText(panel, label='Email:')
        self.email_text = wx.TextCtrl(panel)


        self.salary_label = wx.StaticText(panel, label='Salary:')
        self.salary_text = wx.TextCtrl(panel)

        # Create submit button
        self.submit_button = wx.Button(panel, label='Submit')
        self.submit_button.Bind(wx.EVT_BUTTON, self.on_submit)

        # Bind Enter key event to text controls
        self.name_text.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
        self.age_text.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
        self.email_text.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
        self.salary_text.Bind(wx.EVT_KEY_DOWN, self.on_key_down)

        # Create sizer for layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.name_label, 0, wx.ALL, 5)
        sizer.Add(self.name_text, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.age_label, 0, wx.ALL, 5)
        sizer.Add(self.age_text, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.email_label, 0, wx.ALL, 5)
        sizer.Add(self.email_text, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.salary_label,0,wx.ALL, 5)
        sizer.Add(self.salary_text,0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.submit_button, 0, wx.ALL | wx.ALIGN_CENTER, 5)

        panel.SetSizer(sizer)
        self.Show()

    def on_key_down(self, event):
        # Check if the Enter key is pressed
        if event.GetKeyCode() == wx.WXK_RETURN:
            # Move focus to the next text control
            current = self.FindFocus()
            if current == self.name_text:
                self.age_text.SetFocus()
            elif current == self.age_text:
                self.email_text.SetFocus()
            elif current == self.email_text:
                self.salary_text.SetFocus()  
            elif current == self.salary_text:
                self.submit_button.SetFocus()    # Optionally focus the submit button
            return  # Skip the default event handler
        event.Skip()  # Allow other events to be processed    

    def on_submit(self, event):
        name = self.name_text.GetValue()
        age = self.age_text.GetValue()
        email = self.email_text.GetValue()
        salary = self.salary_text.GetValue()

        wx.MessageBox(f'Name: {name}\nAge: {age}\nEmail: {email}\nSalary: {salary}', 'Submitted Information', wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App(False)
    frame = FillUpForm()
    app.MainLoop()
