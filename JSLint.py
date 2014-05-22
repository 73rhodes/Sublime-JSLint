#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
import re
import os

EXEC_LINT = 'js_lint_exec'
SETTINGS_FILE = 'JSLint.sublime-settings'

class JsLintExecCommand(sublime_plugin.WindowCommand):

	def run(self, files=[]):
		settings = sublime.load_settings(SETTINGS_FILE)
		self.window.run_command('exec', {
			'cmd':
				list(map(os.path.expanduser, settings.get('jslint', ['node', sublime.packages_path() + '/JSLint/linter.js']))) +
				settings.get('options', []) +
				files,
			'line_regex': settings.get('line_regex', '.*// Line ([0-9]*), Pos ([0-9]*)$'),
			'file_regex': settings.get('file_regex', '(^[^# ]+.*$)')
		})


class JsLintOnSave(sublime_plugin.EventListener):

	def on_post_save(self, view):
		settings = sublime.load_settings(SETTINGS_FILE)
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
