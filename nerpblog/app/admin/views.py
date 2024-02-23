from flask_admin.contrib.sqla import ModelView

class ABSView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True
    column_default_sort = ('id', True)
    column_filters = ['id']

class UserView(ABSView):
    column_list = ['id', 'name', 'tgid', 'tglink']
    column_searchable_list = ['name']
    form_columns = ['name', 'tgid', 'tglink']

class PostView(ABSView):
    column_list = ['id', 'title', 'date', 'userid'] 
    column_searchable_list = ['title', 'htmltext'] 
    form_columns = ['htmltext', 'title', 'media', 'date', 'likes', 'userid'] 

class CommentView(ABSView):
    column_list = ['id', 'text', 'date', 'userid', 'postid']  
    column_searchable_list = ['text'] 
    form_columns = ['text', 'date', 'userid', 'postid']  
