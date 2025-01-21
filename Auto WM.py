from PIL import Image as PIL_Image
from tkinter import *
from tkinter import ttk, messagebox, filedialog, font, colorchooser
from Autocomplete_Combo import AutocompleteCombobox
import os
from PIL import ImageFont, ImageDraw


class AutoWM:
    # Main Variables
    title = "Auto WM"
    iconPath = "ico.ico"
    wSize, hSize = 500, 450
    mainLbg = '#3C3F41'
    mainFg = '#A2A2A2'
    mainDbg = '#2B2B2B'
    mainWbg = '#45494A'
    mainWbd = '#646464'
    mainWhBg = '#3D6185'
    mainWfg = '#BBBBBB'

    def __init__(self, wind) -> None:
        self.root = wind
        self.root.title(self.title)
        self.root.iconbitmap(self.iconPath)
        self.root.config(bg=self.mainLbg)

        self.root.minsize(self.wSize, self.hSize)
        self.root.maxsize(self.wSize, self.hSize)
        self.root.lift()
        # self.root.attributes('-topmost', True)
        self.root.focus_force()

        # Variables
        self.var_img = StringVar()
        self.var_wmk = StringVar()
        self.var_txt = StringVar()
        self.var_fnt = StringVar()
        self.var_siz = StringVar()
        self.var_clr = StringVar()
        self.var_log = StringVar()
        self.var_wid = StringVar()
        self.var_hit = StringVar()
        self.var_alp = IntVar()
        self.var_loc = StringVar()
        self.var_out = StringVar()

        self.var_x = StringVar()
        self.var_y = StringVar()

        self.isFolder_Image_Images = 0  # 0 for not selected 1 for folder 2 for image 3 for images
        self.isError = True

        # TTk Style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground=self.mainWbg, background=self.mainWbg)

        y_space = 40
        y_ = y_space
        lbl_img = Label(self.root, text='Image Path', font="calibri", bg=self.mainLbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        lbl_img.place(x=20, y=y_)
        ent_img = Entry(self.root, textvariable=self.var_img, border=0, font="calibri", bg=self.mainWbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        ent_img.place(x=130, y=y_, width=270)
        self.root.update()
        btn_openImage = Button(self.root, command=self.open_image, justify=LEFT, text='+', font=('wingdings', 15), bd=0, cursor='hand2', bg=self.mainLbg, activeforeground=self.mainDbg, activebackground=self.mainLbg, fg=self.mainWfg)
        btn_openImage.place(x=400, y=y_, width=30, height=25)
        btn_openImages = Button(self.root, command=self.open_images, justify=LEFT, text='4', font=('wingdings', 15), bd=0, cursor='hand2', bg=self.mainLbg, activeforeground=self.mainDbg, activebackground=self.mainLbg, fg=self.mainWfg)
        btn_openImages.place(x=430, y=y_, width=30, height=25)
        btn_openFolder = Button(self.root, command=self.open_folder, justify=LEFT, text='1', font=('wingdings', 15), bd=0, cursor='hand2', bg=self.mainLbg, activeforeground=self.mainDbg, activebackground=self.mainLbg, fg=self.mainWfg)
        btn_openFolder.place(x=460, y=y_, width=30, height=25)

        def wmk(e):
            def img_():
                lbl_txt.place_forget()
                ent_txt.place_forget()
                lbl_fnt.place_forget()
                ent_fnt.place_forget()
                lbl_siz.place_forget()
                ent_siz.place_forget()
                lbl_clr.place_forget()
                ent_clr.place_forget()
                self.btn_clr.place_forget()

                y_ = self.y_wm
                lbl_log.place_configure(x=20, y=y_)
                ent_log.place_configure(x=130, y=y_, width=330)
                btn_log.place_configure(x=460, y=y_, width=30, height=25)
                y_ += y_space
                lbl_w_h.place_configure(x=20, y=y_)
                ent_wid.place_configure(x=130, y=y_, width=180)
                ent_hit.place_configure(x=130 + 181, y=y_, width=179)
                y_ += y_space
                lbl_alp.place_configure(x=20, y=y_)
                ent_alp.place_configure(x=130, y=y_, width=360)

            if self.var_wmk.get() == "Image":
                img_()
            elif self.var_wmk.get() == "Text":
                lbl_log.place_forget()
                ent_log.place_forget()
                btn_log.place_forget()
                lbl_w_h.place_forget()
                ent_wid.place_forget()
                ent_hit.place_forget()
                lbl_alp.place_forget()
                ent_alp.place_forget()

                y_ = self.y_wm
                lbl_txt.place_configure(x=20, y=y_)
                ent_txt.place_configure(x=130, y=y_, width=360)
                y_ += y_space
                lbl_fnt.place_configure(x=20, y=y_)
                ent_fnt.place_configure(x=130, y=y_, width=360)
                y_ += y_space
                lbl_siz.place_configure(x=20, y=y_)
                ent_siz.place_configure(x=130, y=y_, width=360)
                y_ += y_space
                lbl_clr.place_configure(x=20, y=y_)
                ent_clr.place_configure(x=130, y=y_, width=330)
                self.btn_clr.place_configure(x=460, y=y_, width=30, height=25)
            else:
                self.var_wmk.set("Image")
                img_()
        y_ += y_space
        lbl_wmk = Label(self.root, text='Water Mark', font="calibri", bg=self.mainLbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        lbl_wmk.place(x=20, y=y_)
        lst_wmk = ['Text', 'Image']
        ent_wmk = AutocompleteCombobox(self.root, values=lst_wmk, textvariable=self.var_wmk, font="calibri", background=self.mainWbg, foreground=self.mainWfg)
        ent_wmk.set_completion_list(lst_wmk)
        ent_wmk.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.mainWbg}' % ent_wmk)
        ent_wmk.place(x=130, y=y_, width=360)
        ent_wmk.current(0)
        ent_wmk.bind('<<ComboboxSelected>>', wmk)

        y_ += y_space
        self.y_wm = y_
        lbl_txt = Label(self.root, text='Text', font="calibri", bg=self.mainLbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        lbl_txt.place(x=20, y=y_)
        ent_txt = Entry(self.root, textvariable=self.var_txt, border=0, font="calibri", bg=self.mainWbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        ent_txt.place(x=130, y=y_, width=360)
        self.var_txt.set('Water Mark')

        y_ += y_space
        lbl_fnt = Label(self.root, text='Font', font="calibri", bg=self.mainLbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        lbl_fnt.place(x=20, y=y_)
        lst_fnt = list(font.families())
        ent_fnt = AutocompleteCombobox(self.root, values=lst_fnt, textvariable=self.var_fnt, font="calibri", background=self.mainWbg, foreground=self.mainWfg)
        ent_fnt.set_completion_list(lst_fnt)
        ent_fnt.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.mainWbg}' % ent_fnt)
        ent_fnt.place(x=130, y=y_, width=360)
        ent_fnt.current(0)
        self.var_fnt.set('calibri')

        y_ += y_space
        lbl_siz = Label(self.root, text='Size', font="calibri", bg=self.mainLbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        lbl_siz.place(x=20, y=y_)
        ent_siz = Entry(self.root, textvariable=self.var_siz, border=0, font="calibri", bg=self.mainWbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        ent_siz.place(x=130, y=y_, width=360)
        self.var_siz.set('30')

        y_ += y_space
        lbl_clr = Label(self.root, text='Color', font="calibri", bg=self.mainLbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        lbl_clr.place(x=20, y=y_)
        ent_clr = Entry(self.root, textvariable=self.var_clr, border=0, font="calibri", state=DISABLED, bg=self.mainWbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        ent_clr.place(x=130, y=y_, width=330)
        self.btn_clr = Button(self.root, command=self.choose_color, justify=LEFT, text='🎨', font=('calibri', 13), bd=0, cursor='hand2', bg=self.mainLbg, activeforeground=self.mainDbg, activebackground=self.mainLbg, fg=self.mainWfg)
        self.btn_clr.place(x=460, y=y_, width=30, height=25)
        self.var_clr.set('#ffffff')
        self.btn_clr.config(fg='#ffffff')

        lbl_log = Label(self.root, text='Logo', font="calibri", bg=self.mainLbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        lbl_log.place(x=20, y=y_)
        ent_log = Entry(self.root, textvariable=self.var_log, border=0, font="calibri", bg=self.mainWbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        ent_log.place(x=130, y=y_, width=330)
        btn_log = Button(self.root, command=self.open_logo, justify=LEFT, text='+', font=('wingdings', 15), bd=0, cursor='hand2', bg=self.mainLbg, activeforeground=self.mainDbg, activebackground=self.mainLbg, fg=self.mainWfg)
        btn_log.place(x=460, y=y_, width=30, height=25)

        lbl_w_h = Label(self.root, text='Width, Height', font="calibri", bg=self.mainLbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        lbl_w_h.place(x=20, y=y_)
        ent_wid = Entry(self.root, textvariable=self.var_wid, border=0, font="calibri", bg=self.mainWbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        ent_wid.place(x=130, y=y_, width=180)
        ent_hit = Entry(self.root, textvariable=self.var_hit, border=0, font="calibri", bg=self.mainWbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        ent_hit.place(x=130 + 181, y=y_, width=179)
        self.var_wid.set('0')
        self.var_hit.set('0')

        lbl_alp = Label(self.root, text='Alpha', font="calibri", bg=self.mainLbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        lbl_alp.place(x=20, y=y_)
        ent_alp = Scale(self.root, orient=HORIZONTAL, variable=self.var_alp, from_=0, to=255, border=0, font="calibri", bg=self.mainWbg, activebackground=self.mainDbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        ent_alp.place(x=130, y=y_, width=360)

        lbl_txt.place_forget()
        ent_txt.place_forget()
        lbl_fnt.place_forget()
        ent_fnt.place_forget()
        lbl_siz.place_forget()
        ent_siz.place_forget()
        lbl_clr.place_forget()
        ent_clr.place_forget()
        self.btn_clr.place_forget()

        lbl_log.place_forget()
        ent_log.place_forget()
        btn_log.place_forget()
        lbl_w_h.place_forget()
        ent_wid.place_forget()
        ent_hit.place_forget()
        lbl_alp.place_forget()
        ent_alp.place_forget()

        y_ += y_space
        lbl_loc = Label(self.root, text='Location', font="calibri", bg=self.mainLbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        lbl_loc.place(x=20, y=y_)
        lst_loc = ["Left", "Right", "Up", "Down", "Center", "Left Down", "Left Up", "Right Down", "Right Up"]
        ent_loc = AutocompleteCombobox(self.root, values=lst_loc, textvariable=self.var_loc, font="calibri", background=self.mainWbg, foreground=self.mainWfg)
        ent_loc.set_completion_list(lst_loc)
        ent_loc.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.mainWbg}' % ent_loc)
        ent_loc.place(x=130, y=y_, width=360)
        ent_loc.current(0)

        y_ += y_space
        lbl_out = Label(self.root, text='Save Location', font="calibri", bg=self.mainLbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        lbl_out.place(x=20, y=y_)
        ent_out = Entry(self.root, textvariable=self.var_out, border=0, font="calibri", bg=self.mainWbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        ent_out.place(x=130, y=y_, width=330)
        btn_out = Button(self.root, command=self.open_out, justify=LEFT, text='=', font=('wingdings', 15), bd=0, cursor='hand2', bg=self.mainLbg, activeforeground=self.mainDbg, activebackground=self.mainLbg, fg=self.mainWfg)
        btn_out.place(x=460, y=y_, width=30, height=25)

        y_ += y_space
        btn_border_saveImage = Entry(self.root, border=0, font="calibri", disabledbackground=self.mainWbg, state=DISABLED, disabledforeground=self.mainWfg)
        btn_border_saveImage.place(x=395, y=y_-5, width=100, height=35)
        btn_saveImage = Button(self.root, command=self.save_image, justify=LEFT, text='Save', font=('calibri', 15), bd=0, cursor='hand2', bg=self.mainLbg, activeforeground=self.mainDbg, activebackground=self.mainLbg, fg=self.mainWfg)
        btn_saveImage.place(x=400, y=y_, width=90, height=25)

        y_ += y_space
        lbl_abt = Label(self.root, text='Created By Abdullah Ahmad', font="calibri", bg=self.mainLbg, fg=self.mainWfg, highlightbackground=self.mainWbd, highlightthickness=2, highlightcolor=self.mainWhBg)
        lbl_abt.place(x=20, y=y_, width=460)

        wmk('e')

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose color")
        if color_code[1] != "" and color_code[1] != None:
            self.var_clr.set(color_code[1])
            self.btn_clr.config(fg=color_code[1])

    def open_folder(self):
        folderName = filedialog.askdirectory(title='Select Folder Of Images')
        if folderName != '':
            self.isFolder_Image_Images = 1
            self.var_img.set(folderName)
            self.checkSupportedFormat(folderName)

    def open_image(self):
        imageName = filedialog.askopenfilename(title='Select Image')
        if imageName != '':
            self.isFolder_Image_Images = 2
            self.var_img.set(imageName)
            self.checkSupportedFormat(imageName)

    def open_images(self):
        imagesName = filedialog.askopenfilenames(title='Select Images')
        if imagesName != '':
            self.isFolder_Image_Images = 3
            self.var_img.set(imagesName)
            self.checkSupportedFormat(imagesName)

    def open_logo(self):
        imageName = filedialog.askopenfilename(title='Select Image', filetypes=(('PNG', '*.png'), ('JPG', '*.jpg'), ('All Files', '*.*')))
        if imageName != '':
            self.var_log.set(imageName)

    def open_out(self):
        folderName = filedialog.askdirectory(title='Select Folder Where You Want To Save')
        if folderName != '':
            self.var_out.set(folderName)

    def save_image(self):
        def multiple(type_):
            try:
                if type_ == 'T':
                    fn = self.var_img.get()
                    fn = fn.replace('(', '')
                    fn = fn.replace(')', '')
                    fn = fn.replace('\'', '')
                    fn = fn.split(',')
                    fn = [i.lstrip() for i in fn]
                    sl = self.var_out.get()

                    er = 0
                    ne = 0
                    el = []
                    for i in fn:
                        if i.rstrip('\n').rstrip(' ') != '':
                            name = os.path.basename(i)
                            try:
                                name, *_, ext = name.split('.')
                                try:
                                    image = PIL_Image.open(i).convert('RGBA')
                                except:
                                    image = PIL_Image.open(i)
                                watermark_image = image.copy()

                                draw = ImageDraw.Draw(watermark_image)
                                font = ImageFont.truetype(self.var_fnt.get(), int(self.var_siz.get()))
                                bw, bh = watermark_image.size
                                _, _, fw, fh = font.getbbox(self.var_txt.get())
                                self.check_xny(bw, bh, fw, fh)
                                draw.text((int(self.var_x.get()), int(self.var_y.get())), self.var_txt.get(), self.var_clr.get(), font=font)

                                saveLoc = f'{sl}/{name}-Edited.{ext}'
                                try:
                                    watermark_image.save(saveLoc)
                                except:
                                    watermark_image = watermark_image.convert('RGB')
                                    watermark_image.save(saveLoc)
                                ne += 1
                            except Exception as e:
                                er += 1
                                el.append(f"{i} | {e}")

                    if er == 0:
                        messagebox.showinfo('Conversion Successfully Completed', f'Total Images Found: {ne}\nAll Your image Successfully Converted')
                    else:
                        messagebox.showerror(f'Conversion Successfully Completed With {er} Error', f'Total Images found: {ne+er}\nSuccessfully Converted: {ne}\nError In Conversion: {er}\nError In These Files: {el}')

                elif type_ == 'I':
                    fn = self.var_img.get()
                    fn = fn.replace('(', '')
                    fn = fn.replace(')', '')
                    fn = fn.replace('\'', '')
                    fn = fn.split(',')
                    fn = [i.lstrip() for i in fn]
                    sl = self.var_out.get()

                    er = 0
                    ne = 0
                    el = []
                    for i in fn:
                        name = os.path.basename(i)
                        try:
                            name, *_, ext = name.split('.')

                            try:
                                image = PIL_Image.open(i).convert('RGBA')
                            except:
                                image = PIL_Image.open(i)
                            Image1copy = image.copy()
                            try:
                                Image2 = PIL_Image.open(self.var_log.get()).convert('RGBA')
                            except:
                                Image2 = PIL_Image.open(self.var_log.get())
                            Image2copy = Image2.copy()

                            if self.var_wid.get() != '0' and self.var_hit.get() != '0':
                                Image2copy = Image2copy.resize((int(self.var_wid.get()), int(self.var_hit.get())))

                            if self.var_alp.get() != 0:
                                Image2copy.putalpha(self.var_alp.get())

                            bw, bh = Image1copy.size
                            fw, fh = Image2copy.size
                            self.check_xny(bw, bh, fw, fh)
                            Image1copy.paste(Image2copy, (int(self.var_x.get()), int(self.var_y.get())), mask=Image2copy)

                            saveLoc = f'{sl}/{name}-Edited.{ext}'
                            try:
                                Image1copy.save(saveLoc)
                            except:
                                Image1copy = Image1copy.convert('RGB')
                                Image1copy.save(saveLoc)
                            ne += 1
                        except Exception as e:
                            er += 1
                            el.append(f"{i} | {e}")

                    if er == 0:
                        messagebox.showinfo('Conversion Successfully Completed', f'Total Images Found: {ne}\nAll Your image Successfully Converted')
                    else:
                        messagebox.showerror(f'Conversion Successfully Completed With {er} Error', f'Total Images found: {ne+er}\nSuccessfully Converted: {ne}\nError In Conversion: {er}\nError In These Files: {el}')

            except Exception as e:
                messagebox.showerror('Error', e)
        def single(type_):
            if type_ == 'T':
                try:
                    fn = self.var_img.get()
                    sl = self.var_out.get()

                    name = os.path.basename(fn)
                    name, *_, ext = name.split('.')
                    try:
                        image = PIL_Image.open(fn).convert('RGBA')
                    except:
                        image = PIL_Image.open(fn)
                    watermark_image = image.copy()
                    draw = ImageDraw.Draw(watermark_image)
                    font = ImageFont.truetype(self.var_fnt.get(), int(self.var_siz.get()))

                    bw, bh = watermark_image.size
                    _, _, fw, fh = font.getbbox(self.var_txt.get())
                    self.check_xny(bw, bh, fw, fh)
                    draw.text((int(self.var_x.get()), int(self.var_y.get())), self.var_txt.get(), self.var_clr.get(), font=font)

                    saveLoc = f'{sl}/{name}-Edited.{ext}'
                    try:
                        watermark_image.save(saveLoc)
                    except:
                        watermark_image = watermark_image.convert('RGB')
                        watermark_image.save(saveLoc)

                    messagebox.showinfo('Water Mark Added Successfully', f'Water Mark Added Successfully\nImage:{fn}\nOutput:{sl}/{name}-Edited.{ext}')
                except Exception as e:
                    messagebox.showerror(f'Error', f'While Adding Water Mark We Found Error: {e}')

            elif type_ == 'I':
                try:
                    fn = self.var_img.get()
                    sl = self.var_out.get()

                    name = os.path.basename(fn)
                    name, *_, ext = name.split('.')
                    try:
                        image = PIL_Image.open(fn).convert('RGBA')
                    except:
                        image = PIL_Image.open(fn)
                    Image1copy = image.copy()
                    try:
                        Image2 = PIL_Image.open(self.var_log.get()).convert('RGBA')
                    except:
                        Image2 = PIL_Image.open(self.var_log.get())
                    Image2copy = Image2.copy()

                    if self.var_wid.get() != '0' and self.var_hit.get() != '0':
                        Image2copy = Image2copy.resize((int(self.var_wid.get()), int(self.var_hit.get())))

                    if self.var_alp.get() != 0:
                        Image2copy.putalpha(self.var_alp.get())

                    bw, bh = Image1copy.size
                    fw, fh = Image2copy.size
                    self.check_xny(bw, bh, fw, fh)
                    Image1copy.paste(Image2copy, (int(self.var_x.get()), int(self.var_y.get())), mask=Image2copy)

                    saveLoc = f'{sl}/{name}-Edited.{ext}'
                    try:
                        Image1copy.save(saveLoc)
                    except:
                        Image1copy = Image1copy.convert('RGB')
                        Image1copy.save(saveLoc)
                    messagebox.showinfo('Water Mark Added Successfully', f'Water Mark Added Successfully\nImage:{fn}\nOutput:{sl}/{name}-Edited.{ext}')
                except Exception as e:
                    messagebox.showerror(f'Error', f'While Adding Water Mark We Found Error: {e}')

        if not self.isError:
            if self.isFolder_Image_Images == 0:
                messagebox.showerror('Error', 'First Select The Image Path Or Any Folder')
            elif self.var_img.get() == '':
                messagebox.showerror('Error', 'First Select The Images')
            elif self.var_loc.get() == '':
                messagebox.showerror('Error', 'First Select The Location')
            elif self.var_out.get() == '':
                messagebox.showerror('Error', 'First Select The Save Location')
            elif self.var_wmk.get() == 'Text':
                if self.var_txt.get() == '':
                    messagebox.showerror('Error', 'First Enter The Text')
                elif self.var_fnt.get() == '':
                    messagebox.showerror('Error', 'First Select The Font')
                elif self.var_siz.get() == '':
                    messagebox.showerror('Error', 'First Select The Size')
                elif self.var_clr.get() == '':
                    messagebox.showerror('Error', 'First Select The Color')
                elif self.isFolder_Image_Images == 1 or self.isFolder_Image_Images == 3:
                    multiple('T')
                elif self.isFolder_Image_Images == 2:
                    single('T')
                else:
                    messagebox.showerror('Error', 'First Select The Image Path Or Any Folder\nAnd also Save Location')

            elif self.var_wmk.get() == 'Image':
                if self.var_log.get() == '':
                    messagebox.showerror('Error', 'First Select The Logo')
                elif self.var_wid.get() == '':
                    messagebox.showerror('Error', 'First Enter The Width')
                elif self.var_hit.get() == '':
                    messagebox.showerror('Error', 'First Enter The Height')
                elif self.isFolder_Image_Images == 1 or self.isFolder_Image_Images == 3:
                    multiple('I')
                elif self.isFolder_Image_Images == 2:
                    single('I')
                else:
                    messagebox.showerror('Error', 'First Select The Image Path Or Any Folder\nAnd also Save Location')

            else:
                messagebox.showerror('Error', 'First Select The Image Path Or Any Folder\nAnd also Save Location')
        else:
            messagebox.showerror('Error', 'First Select The Image Path Or Any Folder\nAnd also Save Location')

    def checkSupportedFormat(self, path):
        if self.isFolder_Image_Images == 1:
            filenames = next(os.walk(path), (None, None, []))[2]
            filenames_ = []
            for i in filenames:
                filenames_.append(path+'/'+i)
            countError = 0
            countSuccess = 0
            fetched = []
            ext_l = []
            for path_ in filenames_:
                name = os.path.basename(path_)
                path = os.path.splitext(path_)
                fullname, ext = path[0], path[1]

                abcd = PIL_Image.registered_extensions()
                er = 0
                for i in abcd.items():
                    if i[0] == ext:
                        er = 1
                        self.isError = False
                        fetched.append(path_)
                        countSuccess += 1
                if er == 0:
                    ext_l.append(f'{ext}')
                    countError += 1
            ext_l = set(ext_l)
            ext_l = list(ext_l)
            if len(ext_l) != 0:
                messagebox.showinfo(title="Error", message=f"Total Founded = {countError+countSuccess}\nTotal Image Found = {countSuccess}\nExtensions Not Supported = {countError}\nSorry We Can't Support These Formats: {ext_l}")
            else:
                messagebox.showinfo(title="Error", message=f"Total Images Found = {countSuccess}")
            self.var_img.set(fetched)

        elif self.isFolder_Image_Images == 2:
            name = os.path.basename(path)
            path = os.path.splitext(path)
            fullname, ext = path[0], path[1]

            abcd = PIL_Image.registered_extensions()
            er = 0
            for i in abcd.items():
                if i[0] == ext:
                    er = 1
                    self.isError = False
                    break
            if er == 0:
                messagebox.showerror(title="Error", message=f"Sorry At This Time We Can't Support {ext} Format")
                self.isError = True

        elif self.isFolder_Image_Images == 3:
            countError = 0
            countSuccess = 0
            fetched = []
            ext_l = []
            for path_ in path:
                name = os.path.basename(path_)
                path = os.path.splitext(path_)
                fullname, ext = path[0], path[1]

                abcd = PIL_Image.registered_extensions()
                er = 0
                for i in abcd.items():
                    if i[0] == ext:
                        er = 1
                        self.isError = False
                        fetched.append(path_)
                        countSuccess += 1
                if er == 0:
                    ext_l.append(f'{ext}')
                    countError += 1
            ext_l = set(ext_l)
            ext_l = list(ext_l)
            if len(ext_l) != 0:
                messagebox.showinfo(title="Error", message=f"Total Founded = {countError+countSuccess}\nTotal Image Found = {countSuccess}\nExtensions Not Supported = {countError}\nSorry We Can't Support These Formats: {ext_l}")
            else:
                messagebox.showinfo(title="Error", message=f"Total Images Found = {countSuccess}")
            self.var_img.set(fetched)

    def check_xny(self, bw, bh, fw, fh):

        if self.var_loc.get() == 'Left':
            self.var_x.set(0)
            self.var_y.set(int((bh - fh) / 2))
        elif self.var_loc.get() == 'Right':
            self.var_x.set(bw - fw)
            self.var_y.set(int((bh - fh) / 2))
        elif self.var_loc.get() == 'Up':
            self.var_x.set(int((bw - fw) / 2))
            self.var_y.set(0)
        elif self.var_loc.get() == 'Down':
            self.var_x.set(int((bw - fw) / 2))
            self.var_y.set(bh - fh)
        elif self.var_loc.get() == 'Center':
            self.var_x.set(int((bw - fw) / 2))
            self.var_y.set(int((bh - fh) / 2))
        elif self.var_loc.get() == 'Right Up':
            self.var_x.set(bw - fw)
            self.var_y.set(0)
        elif self.var_loc.get() == 'Right Down':
            self.var_x.set(bw - fw)
            self.var_y.set(bh - fh)
        elif self.var_loc.get() == 'Left Up':
            self.var_x.set(0)
            self.var_y.set(0)
        elif self.var_loc.get() == 'Left Down':
            self.var_x.set(0)
            self.var_y.set(bh - fh)


if __name__ == '__main__':
    root = Tk()
    obj = AutoWM(root)
    root.mainloop()
