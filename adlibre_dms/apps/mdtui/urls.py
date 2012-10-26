"""
Module: Metadata Template UI URLS
Project: Adlibre DMS
Copyright: Adlibre Pty Ltd 2012
License: See LICENSE for license information
"""

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('mdtui.views',
    # Home
    url(r'^$', direct_to_template, {'template': 'mdtui/home.html'}, name='mdtui-home'),
    # Search
    url(r'^search/type$', 'search_type', {'step':'type',}, name='mdtui-search'),
    url(r'^search/type', 'search_type', {'step':'type',}, name='mdtui-search-type'),
    url(r'^search/options$', 'search_options', {'step':'options',}, name='mdtui-search-options'),
    url(r'^search/results$', 'search_results', {'step':'results',}, name='mdtui-search-results'),
    url(r'^search/export/$', 'search_results', {'step':'export'}, name='mdtui-search-export'),
    # Indexing
    url(r'^indexing/type$', 'indexing_select_type', {'step':'1',}, name='mdtui-index-type'),
    url(r'^indexing/details$', 'indexing_details', {'step':'2',}, name='mdtui-index-details'),
    url(r'^indexing/source$', 'indexing_source', {'step':'3',}, name='mdtui-index-source'),
    url(r'^indexing/finished$', 'indexing_finished', {'step':'4',}, name='mdtui-index-finished'),
    url(r'^indexing/edit/(?P<code>[\w_-]+)$', 'indexing_edit', {'step': 'edit'}, name='mdtui-index-edit'),
    url(r'^indexing/edit_finished$', 'indexing_edit_result', {'step': 'edit_finish'}, name='mdtui-index-edit-finished'),
    # Common
    url(r'^download/(?P<code>[\w_-]+)$', 'download_pdf', name='mdtui-download-pdf'),
    url(r'^view/(?P<code>[\w_-]+)$', 'view_pdf', {'step':'view',}, name='mdtui-view-pdf'),
    # AJAX
    url(r'^parallel/$', 'mdt_parallel_keys', name='mdtui-parallel-keys'),
)

urlpatterns += patterns('mdtui.upload_handler_views',
    url(r'^upload_progress/$', 'upload_progress', name='mdtui-upload-progress'),
)