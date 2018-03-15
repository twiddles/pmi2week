import numpy as np
import pandas as pd
import re
import regex
import utils
from spacy import displacy
from gensim import models 
from traitlets import Int, Instance, Unicode, Set, Bool, link, HasTraits


class Worker(HasTraits):
    sno,pe,ie,se = Int(0), Int(0), Int(0), Int(0)
    pre,inf,suf = Unicode(''), Unicode(''), Unicode('')
    pdt,idt,sdt = Set(), Set(), Set()
    popt, iopt, sopt = Bool(True), Bool(True), Bool(True)

    def __init__(self,):
        
        super().__init__()
        self._init_lda_mdl()
        self._init_cf_model()
        

    def _init_lda_mdl(self,):
        print ("Initializing LDA model and scores ...")
        f_mdl="model/lda.model"
        f_aid="06authorDictionary.txt"
        f_scr="data/score_by_author_by_document.p"
        self._mdl = None #models.LdaModel.load(f_mdl)
        self._score_by_author = np.matrix(utils.load_pickle(f_scr))
    
        #bow=mdl.id2word.doc2bow(["this isa test"])

    def _init_cf_model(self,):

        movies_df = pd.read_csv('data/movie_emb.csv', sep = ',', 
                   encoding='utf-8', low_memory=False)
        
        self._mentee_emb = movies_df.as_matrix()

        user_df = pd.read_csv('data/user_emb.csv', sep = ',', 
                   encoding='utf-8', low_memory=False)
        
        self._mentor_emb = user_df.as_matrix()

    def get_mentors_sel_topics(self,mentee):
        vec = np.where(mentee, 1.0/np.sum(mentee) , 0.0)
        auth_ind = self._get_close_mentee(vec)
        return self._compute_mentors(auth_ind)

    def _get_close_mentee(self, mentee):
        return np.argmax(np.dot(mentee, self._score_by_author.T))

    def _compute_mentors(self, auth_ind):
        return np.argmax(np.dot(self._mentee_emb[auth_ind%14000], self._mentor_emb.T))
