# 🍹 Rascals Bar Website - Manager's Guide

Welcome to the website management handbook! This guide shows you how to easily update content, change hours, modify daily specials, refresh menu flyers, and add gallery photos. 

You do not need to know how to write code to keep the website current. A digital assistant handles website tasks seamlessly behind the scenes.

---

## 🪄 Method 1: The Request Assistant (Recommended)

If you need to change text, update hours, rewrite descriptions, or adjust details, you can request changes using plain text.

1. **[Open a New Request Link](https://github.com/adamecker/rascals-site/issues/new)**
2. In the **Title** box, type a brief phrase summarizing what you need (e.g., *Update Saturday Drink Specials*).
3. In the **Leave a comment** box, write exactly what you want changed. 
   * *Example: "Please change the Saturday night highlight text to read: '$4 Cherry Bomb Specials from 10 PM to Midnight' and display it in pink letters."*
4. Look on the right side of the page layout for the **Labels** section. Click the gear icon ⚙️ and select the label named `assistant`.
5. Click the green **Submit new issue** button.

### 👀 Previewing & Approving Your Changes
The Assistant will automatically map the website, locate the correct files, and wrap the code updates into a "Review Package" (called a Pull Request). **Changes do not go live automatically!** You get to test them first:

1. Wait about 1 to 2 minutes after submitting your request.
2. An automated comment will appear in your request thread from **Cloudflare Pages**.
3. Click the temporary **Preview URL** link in that comment to safely view a live test version of the website with your new changes applied.
4. **Need to make an adjustment?** If the preview isn't quite right, do not close the request! Simply type a new comment at the bottom of your original request explaining the tweak (e.g., *"Actually, make the text blue instead of pink"*). The Assistant will wake back up, fix the code, and update the preview link.
5. If the preview looks perfect, go back to the GitHub page and click the green **Merge Pull Request** button to officially publish the updates to the live website!

---

## 📸 Method 2: Adding Gallery Images Automatically

The website layout automatically reads your gallery files. You do not need to edit any files manually to display new bar photos.

1. **[Open the Gallery Upload Folder Link](https://github.com/adamecker/rascals-site/tree/main/public/images)**
2. Click the **Add file** button at the top right, then select **Upload files**.
3. Drag your new photos from your phone or computer directly onto the screen block. **Important Naming Rule:** Ensure your files are named sequentially using the `gallery-N.jpg` format (e.g., `gallery-31.jpg`, `gallery-32.jpg`) so they display in the correct order.
4. Click the green **Commit changes** button at the bottom to save.

### The Automation Rule:
The gallery page dynamically scans the file system. Any image saved in this folder instantly goes into rotation and renders beautifully inside the gallery grids without any manual configuration required.

---

## 📄 Method 3: Updating the Menu Flyers (PDF Upload)

The website features a menu page that converts high-quality layout flyers into web-optimized image files automatically. If your menu pricing or item options change, you only need to save your updated designs into the repository.

1. **[Open the Images Destination Folder Link](https://github.com/adamecker/rascals-site/tree/main/public/images)**
2. Click **Add file** and select **Upload files**.
3. Drag your updated PDF files directly into the window. **They must be named exactly like this:**
   * `menu-1.pdf` (Front Page)
   * `menu-2.pdf` (Back Page)
4. Click the green **Commit changes** button to finalize your upload.

### The Conversion Engine:
An automated system detects the file upload, takes your raw high-resolution layout pages, transforms them into perfectly scaled `.png` image wrappers, and overwrites the active website displays smoothly.

---

## 🛠️ Method 4: Modifying Site Text Logs Manually

If you need to tweak data entries immediately without relying on the Assistant request queue, you can update text fields yourself.

* **[Edit Menu Text Specifications Directly](https://github.com/adamecker/rascals-site/edit/main/src/data/menu.json)**
* **[Edit Specials Schedules & Highlights Directly](https://github.com/adamecker/rascals-site/edit/main/src/data/specials.json)**
* **[Edit Location Info, Forms & Core Settings Directly](https://github.com/adamecker/rascals-site/edit/main/src/data/site.json)**

### Formatting Notice:
When making text edits manually, only update the words inside the straight quotation marks (e.g., change `"Pizza"` to `"Freshly Baked Pizza"`). **Do not alter or delete the quote characters, commas, or curly braces,** as missing punctuation will break the live website application build. Always scroll to the bottom and select the green **Commit Changes** button twice to push updates live.

---

### 🚨 Reverting Mistakes
Every modification is recorded in a secure revision history log. If a layout breaks, items disappear, or unwanted shifts occur, contact your system administrator. The changes can be safely rolled back to a previous date instantly.
