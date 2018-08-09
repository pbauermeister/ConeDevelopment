import wx
import gettext

class MainFrameBase(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AutogeneratedMainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.menu_new = wx.MenuItem(wxglade_tmp_menu, wx.ID_NEW, _("&New...\tCtrl+N"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_new)
        self.menu_open = wx.MenuItem(wxglade_tmp_menu, wx.ID_OPEN, _("&Open...\tCtrl+O"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_open)
        wxglade_tmp_menu.AppendSeparator()
        self.menu_save = wx.MenuItem(wxglade_tmp_menu, wx.ID_SAVE, _("&Save\tCtrl+S"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_save)
        self.menu_save_as = wx.MenuItem(wxglade_tmp_menu, wx.ID_SAVEAS, _("Save As..."), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_save_as)
        wxglade_tmp_menu.AppendSeparator()
        self.menu_print = wx.MenuItem(wxglade_tmp_menu, wx.ID_PRINT, _("&Print...\tCtrl+P"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_print)
        wxglade_tmp_menu.AppendSeparator()
        self.menu_quit = wx.MenuItem(wxglade_tmp_menu, wx.ID_EXIT, _("Quit"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_quit)
        self.frame_menubar.Append(wxglade_tmp_menu, _("&File"))
        wxglade_tmp_menu = wx.Menu()
        self.menu_undo = wx.MenuItem(wxglade_tmp_menu, wx.ID_UNDO, _("&Undo\tCtrl+Z"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_undo)
        self.menu_redo = wx.MenuItem(wxglade_tmp_menu, wx.ID_REDO, _("&Redo\tCtrl+Y"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_redo)
        self.frame_menubar.Append(wxglade_tmp_menu, _("&Edit"))
        wxglade_tmp_menu = wx.Menu()
        self.menu_help = wx.MenuItem(wxglade_tmp_menu, wx.ID_HELP, _("&Help\tF1"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_help)
        self.menu_about = wx.MenuItem(wxglade_tmp_menu, wx.ID_ABOUT, _("&About..."), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_about)
        self.frame_menubar.Append(wxglade_tmp_menu, _("&Help"))
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        self.window_perspective = wx.Window(self, wx.ID_ANY)
        self.label_hint = wx.StaticText(self, wx.ID_ANY, _("hint"))
        self.sizer_11_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Perspective"))
        self.label_7_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Cone radius"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_cone_radius = wx.SpinCtrl(self, wx.ID_ANY, "", min=10, max=1000)
        self.label_8_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Cone height"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_cone_height = wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=1000)
        self.label_10_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Plane tilt"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_plane_tilt = wx.SpinCtrl(self, wx.ID_ANY, "", min=-90, max=90)
        self.sizer_113_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Objects"))
        self.label_2_copy = wx.StaticText(self, wx.ID_ANY, _("Azimuth"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_camera_azimuth = wx.SpinCtrl(self, wx.ID_ANY, "", min=-360, max=360)
        self.label_3_copy = wx.StaticText(self, wx.ID_ANY, _("Altitude"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_camera_altitude = wx.SpinCtrl(self, wx.ID_ANY, "", min=-90, max=90)
        self.label_4_copy = wx.StaticText(self, wx.ID_ANY, _("Distance"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_camera_distance = wx.SpinCtrl(self, wx.ID_ANY, "", min=200, max=10000)
        self.label_5_copy = wx.StaticText(self, wx.ID_ANY, _("FOV"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_camera_fov = wx.SpinCtrl(self, wx.ID_ANY, "", min=30, max=180)
        self.label_camera_pos = wx.StaticText(self, wx.ID_ANY, _("camera"), style=wx.ALIGN_RIGHT)
        self.sizer_112_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Camera"))
        self.window_anamorphosis = wx.Window(self, wx.ID_ANY)
        self.sizer_11_copy_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Cone development"))
        self.button_export_pdf = wx.Button(self, wx.ID_ANY, _("Export PDF..."))
        self.sizer_2_copy_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Document"))
        self.label_7 = wx.StaticText(self, wx.ID_ANY, _("Width"))
        self.spin_ctrl_export_bitmap_width = wx.SpinCtrl(self, wx.ID_ANY, "", min=10, max=100000)
        self.label_13 = wx.StaticText(self, wx.ID_ANY, _("Height"))
        self.spin_ctrl_export_bitmap_height = wx.SpinCtrl(self, wx.ID_ANY, "", min=10, max=100000)
        self.button_export_image = wx.Button(self, wx.ID_ANY, _("Export PNG..."))
        self.sizer_2_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Image"))
        self.button_export_fullscreen = wx.Button(self, wx.ID_ANY, _("Show"))
        self.sizer_2_copy_1_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Fullscreen"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnMenuNew, self.menu_new)
        self.Bind(wx.EVT_MENU, self.OnMenuOpen, self.menu_open)
        self.Bind(wx.EVT_MENU, self.OnMenuSave, self.menu_save)
        self.Bind(wx.EVT_MENU, self.OnMenuSaveAs, self.menu_save_as)
        self.Bind(wx.EVT_MENU, self.OnMenuPrint, self.menu_print)
        self.Bind(wx.EVT_MENU, self.OnMenuQuit, self.menu_quit)
        self.Bind(wx.EVT_MENU, self.OnMenuUndo, self.menu_undo)
        self.Bind(wx.EVT_MENU, self.OnMenuRedo, self.menu_redo)
        self.Bind(wx.EVT_MENU, self.OnMenuHelp, self.menu_help)
        self.Bind(wx.EVT_MENU, self.OnMenuAbout, self.menu_about)
        self.Bind(wx.EVT_SPINCTRL, self.OnConeRadiusSpin, self.spin_ctrl_cone_radius)
        self.Bind(wx.EVT_SPINCTRL, self.OnConeHeightSpin, self.spin_ctrl_cone_height)
        self.Bind(wx.EVT_SPINCTRL, self.OnPlaneTiltSpin, self.spin_ctrl_plane_tilt)
        self.Bind(wx.EVT_SPINCTRL, self.OnCameraAzimuthSpin, self.spin_ctrl_camera_azimuth)
        self.Bind(wx.EVT_SPINCTRL, self.OnCameraAltitudeSpin, self.spin_ctrl_camera_altitude)
        self.Bind(wx.EVT_SPINCTRL, self.OnCameraDistanceSpin, self.spin_ctrl_camera_distance)
        self.Bind(wx.EVT_SPINCTRL, self.OnCameraFovSpin, self.spin_ctrl_camera_fov)
        self.Bind(wx.EVT_BUTTON, self.OnExportPdfClicked, self.button_export_pdf)
        self.Bind(wx.EVT_SPINCTRL, self.OnExportBitmapWidthSpin, self.spin_ctrl_export_bitmap_width)
        self.Bind(wx.EVT_SPINCTRL, self.OnExportBitmapHeightSpin, self.spin_ctrl_export_bitmap_height)
        self.Bind(wx.EVT_BUTTON, self.OnExportImageClicked, self.button_export_image)
        self.Bind(wx.EVT_BUTTON, self.OnShowFullscreenClicked, self.button_export_fullscreen)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AutogeneratedMainFrame.__set_properties
        self.SetTitle(_("ConeDevelopment"))
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("conedevelopment.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.window_perspective.SetBackgroundColour(wx.Colour(225, 225, 225))
        self.label_hint.SetBackgroundColour(wx.Colour(225, 225, 225))
        self.spin_ctrl_cone_radius.SetMinSize((60, 25))
        self.spin_ctrl_cone_height.SetMinSize((60, 25))
        self.spin_ctrl_plane_tilt.SetMinSize((60, 25))
        self.spin_ctrl_camera_azimuth.SetMinSize((60, 25))
        self.spin_ctrl_camera_altitude.SetMinSize((60, 25))
        self.spin_ctrl_camera_distance.SetMinSize((60, 25))
        self.label_5_copy.Hide()
        self.spin_ctrl_camera_fov.SetMinSize((60, 25))
        self.spin_ctrl_camera_fov.Hide()
        self.window_anamorphosis.SetBackgroundColour(wx.Colour(225, 225, 225))
        self.spin_ctrl_export_bitmap_width.SetMinSize((60, 25))
        self.spin_ctrl_export_bitmap_height.SetMinSize((60, 25))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AutogeneratedMainFrame.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_12 = wx.FlexGridSizer(4, 1, 0, 0)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_2_copy_1_staticbox.Lower()
        sizer_2_copy_1 = wx.StaticBoxSizer(self.sizer_2_copy_1_staticbox, wx.VERTICAL)
        sizer_3_copy_1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_2_staticbox.Lower()
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_10 = wx.FlexGridSizer(2, 2, 0, 0)
        self.sizer_2_copy_staticbox.Lower()
        sizer_2_copy = wx.StaticBoxSizer(self.sizer_2_copy_staticbox, wx.VERTICAL)
        sizer_3_copy = wx.BoxSizer(wx.VERTICAL)
        self.sizer_11_copy_staticbox.Lower()
        sizer_11_copy = wx.StaticBoxSizer(self.sizer_11_copy_staticbox, wx.VERTICAL)
        grid_sizer_4_copy = wx.FlexGridSizer(1, 1, 0, 0)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_5 = wx.FlexGridSizer(2, 1, 0, 0)
        self.sizer_112_staticbox.Lower()
        sizer_112 = wx.StaticBoxSizer(self.sizer_112_staticbox, wx.VERTICAL)
        grid_sizer_1121 = wx.FlexGridSizer(5, 2, 0, 0)
        grid_sizer_6 = wx.FlexGridSizer(4, 1, 0, 0)
        self.sizer_113_staticbox.Lower()
        sizer_113 = wx.StaticBoxSizer(self.sizer_113_staticbox, wx.VERTICAL)
        grid_sizer_8 = wx.FlexGridSizer(3, 1, 0, 0)
        grid_sizer_2_copy_1 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_1131 = wx.FlexGridSizer(5, 2, 0, 0)
        grid_sizer_1111 = wx.FlexGridSizer(1, 2, 0, 10)
        self.sizer_11_staticbox.Lower()
        sizer_11 = wx.StaticBoxSizer(self.sizer_11_staticbox, wx.VERTICAL)
        grid_sizer_4 = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_4.Add(self.window_perspective, 1, wx.EXPAND, 0)
        grid_sizer_4.Add(self.label_hint, 0, wx.EXPAND, 0)
        grid_sizer_4.AddGrowableRow(0)
        grid_sizer_4.AddGrowableCol(0)
        sizer_11.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(sizer_11, 1, wx.ALL | wx.EXPAND, 3)
        grid_sizer_1111.AddGrowableCol(0)
        grid_sizer_1131.Add(self.label_7_copy_1, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1131.Add(self.spin_ctrl_cone_radius, 0, wx.ALIGN_RIGHT, 0)
        grid_sizer_1131.Add(self.label_8_copy_1, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1131.Add(self.spin_ctrl_cone_height, 0, wx.ALIGN_RIGHT, 0)
        grid_sizer_1131.Add(self.label_10_copy_1, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1131.Add(self.spin_ctrl_plane_tilt, 0, wx.ALIGN_RIGHT, 0)
        grid_sizer_1131.AddGrowableCol(0)
        grid_sizer_8.Add(grid_sizer_1131, 1, wx.EXPAND, 0)
        grid_sizer_2_copy_1.AddGrowableCol(0)
        grid_sizer_8.Add(grid_sizer_2_copy_1, 1, wx.EXPAND, 0)
        grid_sizer_8.AddGrowableCol(0)
        sizer_113.Add(grid_sizer_8, 1, wx.EXPAND, 0)
        grid_sizer_6.Add(sizer_113, 1, wx.ALL | wx.EXPAND, 3)

        grid_sizer_6.AddGrowableCol(0)
        sizer_1.Add(grid_sizer_6, 1, wx.EXPAND, 0)
        grid_sizer_1121.Add(self.label_2_copy, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1121.Add(self.spin_ctrl_camera_azimuth, 0, 0, 0)
        grid_sizer_1121.Add(self.label_3_copy, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1121.Add(self.spin_ctrl_camera_altitude, 0, 0, 0)
        grid_sizer_1121.Add(self.label_4_copy, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1121.Add(self.spin_ctrl_camera_distance, 0, 0, 0)
        grid_sizer_1121.Add(self.label_5_copy, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1121.Add(self.spin_ctrl_camera_fov, 0, 0, 0)
        grid_sizer_1121.Add(self.label_camera_pos, 0, wx.LEFT | wx.EXPAND | wx.ALIGN_RIGHT, 10)

        grid_sizer_1121.AddGrowableCol(0)
        sizer_112.Add(grid_sizer_1121, 1, wx.EXPAND, 0)
        grid_sizer_5.Add(sizer_112, 1, wx.ALL | wx.EXPAND, 3)
        grid_sizer_5.AddGrowableRow(0)
        grid_sizer_5.AddGrowableRow(1)
        grid_sizer_5.AddGrowableCol(0)
        sizer_1.Add(grid_sizer_5, 1, wx.EXPAND, 0)
        grid_sizer_12.Add(sizer_1, 1, wx.EXPAND, 0)
        grid_sizer_4_copy.Add(self.window_anamorphosis, 1, wx.EXPAND, 0)
        grid_sizer_4_copy.AddGrowableRow(0)
        grid_sizer_4_copy.AddGrowableCol(0)
        sizer_11_copy.Add(grid_sizer_4_copy, 1, wx.EXPAND, 0)
        grid_sizer_12.Add(sizer_11_copy, 1, wx.ALL | wx.EXPAND, 3)
        sizer_3_copy.Add((20, 25), 0, 0, 0)
        sizer_3_copy.Add((20, 25), 0, 0, 0)
        sizer_3_copy.Add(self.button_export_pdf, 0, wx.EXPAND | wx.ALIGN_BOTTOM, 0)
        sizer_2_copy.Add(sizer_3_copy, 1, wx.EXPAND | wx.ALIGN_BOTTOM, 0)
        sizer_4.Add(sizer_2_copy, 1, wx.ALL | wx.EXPAND, 3)
        grid_sizer_10.Add(self.label_7, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_10.Add(self.spin_ctrl_export_bitmap_width, 0, 0, 0)
        grid_sizer_10.Add(self.label_13, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_10.Add(self.spin_ctrl_export_bitmap_height, 0, 0, 0)
        sizer_3.Add(grid_sizer_10, 1, wx.EXPAND, 0)
        sizer_3.Add(self.button_export_image, 0, wx.EXPAND | wx.ALIGN_BOTTOM, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_4.Add(sizer_2, 1, wx.ALL | wx.EXPAND, 3)
        sizer_3_copy_1.Add((20, 25), 0, 0, 0)
        sizer_3_copy_1.Add((20, 25), 0, 0, 0)
        sizer_3_copy_1.Add(self.button_export_fullscreen, 0, wx.EXPAND | wx.ALIGN_BOTTOM, 0)
        sizer_2_copy_1.Add(sizer_3_copy_1, 1, wx.EXPAND | wx.ALIGN_BOTTOM, 0)
        sizer_4.Add(sizer_2_copy_1, 1, wx.ALL | wx.EXPAND, 3)
        grid_sizer_12.Add(sizer_4, 1, 0, 0)
        grid_sizer_12.AddGrowableRow(1)
        grid_sizer_1.Add(grid_sizer_12, 1, wx.EXPAND, 0)
        grid_sizer_1.AddGrowableRow(0)
        grid_sizer_1.AddGrowableCol(0)
        sizer.Add(grid_sizer_1, 1, wx.ALL | wx.EXPAND, 8)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()
        # end wxGlade

    def OnMenuNew(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuNew' not implemented!"
        event.Skip()

    def OnMenuOpen(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuOpen' not implemented!"
        event.Skip()

    def OnMenuSave(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuSave' not implemented!"
        event.Skip()

    def OnMenuSaveAs(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuSaveAs' not implemented!"
        event.Skip()

    def OnMenuPrint(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuPrint' not implemented!"
        event.Skip()

    def OnMenuQuit(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuQuit' not implemented!"
        event.Skip()

    def OnMenuUndo(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuUndo' not implemented!"
        event.Skip()

    def OnMenuRedo(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuRedo' not implemented!"
        event.Skip()

    def OnMenuHelp(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuHelp' not implemented!"
        event.Skip()

    def OnMenuAbout(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuAbout' not implemented!"
        event.Skip()

    def OnConeRadiusSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnConeRadiusSpin' not implemented!"
        event.Skip()

    def OnConeHeightSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnConeHeightSpin' not implemented!"
        event.Skip()

    def OnPlaneTiltSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnPlaneTiltSpin' not implemented!"
        event.Skip()

    def OnCameraAzimuthSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCameraAzimuthSpin' not implemented!"
        event.Skip()

    def OnCameraAltitudeSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCameraAltitudeSpin' not implemented!"
        event.Skip()

    def OnCameraDistanceSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCameraDistanceSpin' not implemented!"
        event.Skip()

    def OnCameraFovSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCameraFovSpin' not implemented!"
        event.Skip()

    def OnExportPdfClicked(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnExportPdfClicked' not implemented!"
        event.Skip()

    def OnExportBitmapWidthSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnExportBitmapWidthSpin' not implemented!"
        event.Skip()

    def OnExportBitmapHeightSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnExportBitmapHeightSpin' not implemented!"
        event.Skip()

    def OnExportImageClicked(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnExportImageClicked' not implemented!"
        event.Skip()

    def OnShowFullscreenClicked(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnShowFullscreenClicked' not implemented!"
        event.Skip()

# end of class AutogeneratedMainFrame

if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    MainFrame = (None, wx.ID_ANY, "")
    app.SetTopWindow(MainFrame)
    MainFrame.Show()
    app.MainLoop()
