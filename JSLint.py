import sublime, sublime_plugin, re

class autoJSLint(sublime_plugin.EventListener):
  def on_post_save(self, view):
    settings = sublime.load_settings("JSLint.sublime-settings")
    if settings.get("run_on_save") and re.search(settings.get("filename_filter"), view.file_name()):
      view.window().run_command( "build" )

class JslintCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.run_command('set_build_system', {
      'file': 'Packages/JSLint/JSLint.sublime-build'
    })
    self.window.run_command('build')
