import sys
import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, cairo

class ZeroVector(Gtk.Window):
    def __init__(self):
        super().__init__(title="Zero Vector - Ultimate Studio")
        self.set_default_size(1400, 900)
        
        self.header = Gtk.HeaderBar()
        self.header.set_show_close_button(True)
        self.header.props.title = ""
        self.header.get_style_context().add_class("hidden-header")
        self.set_titlebar(self.header)
        
        self.setup_css()
        
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.add(main_box)
        
        # ================= LEFT TOOLBAR =================
        self.toolbar_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.toolbar_left.set_size_request(60, -1)
        self.toolbar_left.get_style_context().add_class("toolbar-side")
        main_box.pack_start(self.toolbar_left, False, False, 0)
        
        tools = ["↖️", "✒️", "⬛", "⭕", "T", "✋", "🔍"]
        for t in tools:
            btn = Gtk.Button(label=t)
            btn.get_style_context().add_class("tool-btn")
            self.toolbar_left.pack_start(btn, False, False, 0)
            
        color_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        color_box.get_style_context().add_class("color-picker")
        color_box.set_size_request(35, 35)
        color_box.set_margin_top(20)
        self.toolbar_left.pack_start(color_box, False, False, 0)
        
        # ================= WORKSPACE =================
        self.workspace = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.workspace.get_style_context().add_class("workspace")
        main_box.pack_start(self.workspace, True, True, 0)
        
        top_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        top_bar.get_style_context().add_class("top-bar")
        self.workspace.pack_start(top_bar, False, False, 0)
        
        l_doc = Gtk.Label(label="Vector-Design-1.svg")
        l_doc.get_style_context().add_class("doc-title")
        l_doc.set_margin_start(20)
        top_bar.pack_start(l_doc, False, False, 0)
        
        btn_export = Gtk.Button(label="Export SVG")
        btn_export.get_style_context().add_class("action-btn")
        top_bar.pack_end(btn_export, False, False, 10)
        
        # Infinite Grid Canvas
        self.canvas = Gtk.DrawingArea()
        self.canvas.get_style_context().add_class("canvas-area")
        self.canvas.connect("draw", self.on_draw)
        self.workspace.pack_start(self.canvas, True, True, 0)
        
        # ================= RIGHT PANEL =================
        self.panel_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.panel_right.set_size_request(280, -1)
        self.panel_right.get_style_context().add_class("panel-right")
        main_box.pack_start(self.panel_right, False, False, 0)
        
        l_props = Gtk.Label(label="PROPERTIES")
        l_props.get_style_context().add_class("section-label")
        l_props.set_halign(Gtk.Align.START)
        l_props.set_margin_start(20)
        l_props.set_margin_top(20)
        self.panel_right.pack_start(l_props, False, False, 10)
        
        props = [
            ("X Position", "240.5 px"),
            ("Y Position", "120.0 px"),
            ("Width", "500.0 px"),
            ("Height", "300.0 px"),
            ("Corner Radius", "12 px")
        ]
        
        for name, val in props:
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            vbox.set_margin_start(20)
            vbox.set_margin_end(20)
            vbox.set_margin_bottom(10)
            
            ln = Gtk.Label(label=name)
            ln.get_style_context().add_class("prop-lbl")
            ln.set_halign(Gtk.Align.START)
            
            entry = Gtk.Entry()
            entry.set_text(val)
            entry.get_style_context().add_class("prop-entry")
            
            vbox.pack_start(ln, False, False, 5)
            vbox.pack_start(entry, False, False, 0)
            self.panel_right.pack_start(vbox, False, False, 0)
            
    def on_draw(self, widget, cr):
        width = widget.get_allocated_width()
        height = widget.get_allocated_height()
        
        # Draw background color
        cr.set_source_rgb(0.08, 0.08, 0.08)
        cr.paint()
        
        # Draw Grid
        cr.set_source_rgba(1, 1, 1, 0.05)
        cr.set_line_width(1)
        grid_size = 50
        for i in range(0, width, grid_size):
            cr.move_to(i, 0)
            cr.line_to(i, height)
        for i in range(0, height, grid_size):
            cr.move_to(0, i)
            cr.line_to(width, i)
        cr.stroke()
        
        # Draw Vector object
        cr.set_source_rgba(0.0, 0.6, 1.0, 0.8)
        cr.rectangle(width/2 - 150, height/2 - 100, 300, 200)
        cr.fill_preserve()
        cr.set_source_rgba(1, 1, 1, 1)
        cr.set_line_width(3)
        cr.stroke()
        
        # Draw handles
        cr.set_source_rgb(1, 1, 1)
        cr.rectangle(width/2 - 155, height/2 - 105, 10, 10)
        cr.rectangle(width/2 + 145, height/2 - 105, 10, 10)
        cr.rectangle(width/2 - 155, height/2 + 95, 10, 10)
        cr.rectangle(width/2 + 145, height/2 + 95, 10, 10)
        cr.fill()

    def setup_css(self):
        css = b'''
            window { background-color: #111111; }
            .hidden-header { background: #111111; min-height: 0px; padding: 0px; border: none; box-shadow: none; }
            .toolbar-side { background-color: #1a1a1a; border-right: 1px solid #333333; padding-top: 15px; }
            .tool-btn { background: transparent; color: #FFFFFF; border: none; font-size: 18px; padding: 10px; transition: all 0.2s; border-radius: 6px; margin: 2px 8px; }
            .tool-btn:hover { background: rgba(255,255,255,0.1); }
            .color-picker { background-color: #0099FF; border-radius: 8px; border: 2px solid #FFFFFF; margin-left: 12px; margin-right: 12px; }
            .workspace { background-color: #141414; }
            .top-bar { background-color: #1a1a1a; padding: 10px; border-bottom: 1px solid #000000; }
            .doc-title { color: #FFFFFF; font-size: 14px; font-weight: bold; }
            .action-btn { background: #0066cc; color: #FFFFFF; border: none; border-radius: 6px; font-weight: bold; padding: 6px 15px; }
            .action-btn:hover { background: #0077ee; }
            .panel-right { background-color: #1a1a1a; border-left: 1px solid #333333; }
            .section-label { color: #888888; font-size: 11px; font-weight: 900; letter-spacing: 1px; }
            .prop-lbl { color: #AAAAAA; font-size: 12px; }
            .prop-entry { background: #222222; color: #FFFFFF; border: 1px solid #444444; border-radius: 4px; padding: 5px; font-family: monospace; }
        '''
        provider = Gtk.CssProvider()
        provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

if __name__ == "__main__":
    win = ZeroVector()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
