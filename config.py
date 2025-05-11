# Disable loading of autoconfig.yml to ensure my settings take precedence
config.load_autoconfig(False)

# Basic configuration
c.colors.webpage.preferred_color_scheme = "dark"
c.colors.webpage.darkmode.enabled = True
c.zoom.default = "110%"
# c.content.cookies.accept = "never"


c.fileselect.handler = "external"
c.fileselect.single_file.command = ["alacritty", "-e", "ranger", "--choosefile", "{}"]
c.fileselect.multiple_files.command = [
    "alacritty",
    "-e",
    "ranger",
    "--choosefiles",
    "{}",
]

# cookies
c.content.cookies.accept = "no-3rdparty"
config.set("content.cookies.accept", "all", "*://*.youtube.com/*")
config.set("content.cookies.accept", "all", "*://*.github.com/*")
config.set("content.cookies.accept", "all", "*://*.google.com/*")
config.set("content.cookies.accept", "all", "*://*.chatgpt.com/*")
config.set("content.cookies.accept", "all", "*://*.claude.ai/*")

# Enable scrollbars
# config.set("scrolling.bar", "always")
c.scrolling.bar = "always"

# Resume from where you left off
c.auto_save.session = True

# No crash reports:
c.qt.args = ['no-err-writer']
