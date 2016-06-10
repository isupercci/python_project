# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms


class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
