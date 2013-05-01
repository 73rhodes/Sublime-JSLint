#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
import re
import os

EXEC_LINT = 'js_lint_exec'
LINT_FOLDER = 'js_lint_folder'
SETTINGS_FILE = 'JSLint.sublime-settings'


class JsLintFileCommand(sublime_plugin.WindowCommand):

	def run(self):
		self.window.run_command(EXEC_LINT, {
			'files': [self.window.active_view().file_name()]
		})


class JsLintContainingFolderCommand(sublime_plugin.WindowCommand):

	def run(self):
		self.window.run_command(LINT_FOLDER, {
			'dirs': [os.path.abspath(os.path.join(self.window.active_view().file_name(), os.pardir))]
		})


class JsLintFolderCommand(sublime_plugin.WindowCommand):

	def run(self, dirs):
		settings = sublime.load_settings(SETTINGS_FILE)
		files_to_lint = []
		filename_filter = settings.get('filename_filter')

		for (dirpath, dirnames, filenames) in os.walk(dirs[0]):
			for filename in filenames:
				if re.search(filename_filter, filename):
					files_to_lint.append(os.path.join(dirpath, filename))

		self.window.run_command(EXEC_LINT, {
			'files': files_to_lint
		})

	def is_visible(self, dirs):
		return len(dirs) > 0


class JsLintExecCommand(sublime_plugin.WindowCommand):

	def run(self, files=[]):
		settings = sublime.load_settings(SETTINGS_FILE)
		self.window.run_command('exec', {
			'cmd':
				settings.get('jslint', ['node', sublime.packages_path() + '/JSLint/node_modules/jslint/bin/jslint']) +
				settings.get('options', []) +
				files,
			'line_regex': settings.get('line_regex', '.*// Line ([0-9]*), Pos ([0-9]*)$'),
			'file_regex': settings.get('file_regex', '(^[^# ]+.*$)')
		})


class JsLintOnSave(sublime_plugin.EventListener):

	def on_post_save(self, view):
		settings = sublime.load_settings(SETTINGS_FILE)
		print settings
		if settings.get('run_on_save', False) == False:
			return
		if re.search(settings.get('filename_filter'), view.file_name()):
			view.window().run_command(EXEC_LINT, {
				'files': [view.file_name()]
			})


# Support calls to the old API of the JSLint package.

class JslintCommand(sublime_plugin.WindowCommand):

	def run(self):
		self.window.run_command(EXEC_LINT, {
			'files': [self.window.active_view().file_name()]
		})