import pandas as pd
import numpy as np
from traitlets import Int, Instance, Unicode, link, List
from ipywidgets import Button, VBox, HBox, HTML, Box, Layout, Label, \
                        Text, Textarea, ToggleButtons, HTML, Checkbox, IntSlider, \
                        SelectMultiple, Select

class AppUI(VBox):
    _current_position = Int(0, allow_none = False).tag(sync = True)
    _sel_tops = List();_ment_out=Unicode('')
    _state = Unicode('', allow_none = False).tag(sync = True)

    def __init__(self, 
        worker,
        *args, **kwargs):

        super(VBox, self).__init__(*args, **kwargs)

        self._worker=worker
        self._state, self._rstate = self._init_state()
        self._ment_out=''
        self._num_tops = 50
        self._sel_tops = [False]*self._num_tops
        self._draw()
        #link((self,'_current_position'),(self._rgx_mchr, 'sno'))
        self.observe(self._draw, names='_state')   

        

    def _init_state(self,):
        self._states=["From Topics List", "Write Description", "Search DBPL" ]
        self._rstates=['Recommender 1', 'Recommender 2']
        #self._state=self._states[0]
        return self._states[0], self._rstates[0]

    def _draw(self, change = None):

        form_layout = Layout(display='flex', justify_content='center',align_items='center', width='100%', )
        
        controls = VBox(layout = form_layout)
        controls.children += (Label('Select way to choose your topics:'),ToggleButtons(options=(self._states), 
                                                value=self._state,                                               
                                                #description='Select way to choose your topics:',
                                                disabled=False,),)
        
        link((self,'_state'),(controls.children[1],'value'))

        if self._state==self._states[0]:
            controls.children +=(self._topic_selector(),)

        elif self._state==self._states[1]:
            controls.children +=(self._topic_description(),)

        else:
            controls.children +=(Select(options=['Linux', 'Windows', 'OSX'],
                                                value='OSX',
                                                # rows=10,
                                                description='OS:',
                                                disabled=False),)


        controls.children += (self._make_recmdr_box(),)


        
        
        self.children = (controls,)


    def _topic_selector(self):

        form_item_layout = Layout(width = '100%', 
                             border = 'solid 2px', 
                             margin = '3px', 
                             align_items = 'stretch',
                             padding = '2px')
        #Layout(display = 'flex', flex_flow='row', display_content='center', width='100%', flex_wrap="wrap")
        topic_seltr= HBox(layout = form_item_layout)
        for t in range(self._num_tops):
            name="Topic %d"%t
            topic_seltr.children += (Checkbox(value=self._sel_tops[t], description=name,),)
            topic_seltr.children[-1].observe(lambda chk_bx, num = t: self._update_top(chk_bx, num), names='value')
        return topic_seltr

    def _topic_description(self):
        textarea_layout = Layout(justify_content='center', width='40%', height ='300px')
        return Textarea(layout = textarea_layout)

    def _make_recmdr_box(self):
        form_item_layout = Layout(display='flex', flex_flow='column', align_items='center', width='100%', display_content='center', border='Solid 2px', )
        recom_box= VBox(layout = form_item_layout)
        recom_box.children += ( Label('Choose Recommender:'),
                                ToggleButtons(options=(self._rstates), 
                                                value=self._rstate,                                               
                                                #description='Select way to choose your topics:',
                                                disabled=False),
                                Label(''),
                                Button(description='Make Mentor Recommendation', width = '199 ptx'),
                                HTML(value=self._ment_out),
                                )
        link((self,'_ment_out'),(recom_box.children[-1],'value'))
        recom_box.children[-2].on_click(self._get_mentors)
        return recom_box

    def _update_top(self,change, num):
        self._sel_tops[num] = True
        
    def _get_mentors(self, button):
        if self._state==self._states[0]:
            aid = self._worker.get_mentors_sel_topics(np.asarray(self._sel_tops))
            self._ment_out = str(aid)
            #print ("Work in progress")
            
        if self._state==self._states[1]:
            print ("Work in progress")
        if self._state==self._states[2]:
            print ("Work in progress")