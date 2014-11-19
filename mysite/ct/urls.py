from django.conf.urls import patterns, include, url
from ct.views import *

urlpatterns = patterns('',
    url(r'^$', main_page, name='home'),
    # instructor UI
    # courselet tabs
    url(r'^teach/courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/concepts/$',
        unit_concepts, name='unit_concepts'),
    url(r'^teach/courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/lessons/$',
        unit_lessons, name='unit_lessons'),
    url(r'^teach/courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/resources/$',
        unit_resources, name='unit_resources'),
    # lesson tabs
    url(r'^teach/courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/lessons/(?P<ul_id>\d+)/teach/$',
        ul_teach, name='ul_teach'),
    url(r'^teach/courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/lessons/(?P<ul_id>\d+)/concepts/$',
        ul_concepts, name='ul_concepts'),
    url(r'^teach/courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/lessons/(?P<ul_id>\d+)/errors/$',
        ul_errors, name='ul_errors'),
    url(r'^teach/courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/lessons/(?P<ul_id>\d+)/edit/$',
        edit_lesson, name='edit_lesson'),
    # concept tabs
    url(r'^teach/courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/concepts/(?P<ul_id>\d+)/concepts/$',
        concept_concepts, name='concept_concepts'),
    url(r'^teach/courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/concepts/(?P<ul_id>\d+)/lessons/$',
        concept_lessons, name='concept_lessons'),
    url(r'^teach/courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/concepts/(?P<ul_id>\d+)/errors/$',
        concept_errors, name='concept_errors'),
    url(r'^teach/courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/concepts/(?P<ul_id>\d+)/edit/$',
        edit_lesson, name='edit_concept'),
    # error tabs
    url(r'^teach/courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/errors/(?P<ul_id>\d+)/resolutions/$',
        resolutions, name='resolutions'),
    url(r'^teach/courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/errors/(?P<ul_id>\d+)/edit/$',
        edit_lesson, name='edit_error'),
    # student UI
    # study pages
    url(r'^courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/study/$',
        study_unit, name='study_unit'),
    url(r'^courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/lessons/(?P<ul_id>\d+)/$',
        lesson, name='lesson'),
    url(r'^courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/lessons/(?P<ul_id>\d+)/ask/$',
        ul_respond, name='ul_respond'),
    url(r'^courses/(?P<course_id>\d+)/units/(?P<unit_id>\d+)/lessons/(?P<ul_id>\d+)/responses/(?P<resp_id>\d+)/$',
        assess, name='assess'),
    # deprecated
    url(r'^courses/$', courses, name='courses'),
    url(r'^courses/(?P<course_id>\d+)/$', course, name='course'),
    url(r'^teach/$', teach, name='teach'),
    url(r'^live/$', live_session, name='live'),
    url(r'^live/start/$', live_start, name='livestart'),
    url(r'^live/control/$', live_control, name='control'),
    url(r'^live/end/$', live_end, name='end'),
    url(r'^courses/(?P<course_id>\d+)/study/$', course_study,
        name='course_study'),
    url(r'^courselets/(?P<courselet_id>\d+)/$', courselet, name='courselet'),
    url(r'^courselets/(?P<courselet_id>\d+)/concept/$', courselet_concept,
        name='courselet_concept'),
    url(r'^concepts/$', concepts, name='concepts'),
    url(r'^questions/$', questions, name='questions'),
    url(r'^questions/(?P<ct_id>\d+)/$', question, name='question'),
    url(r'^questions/(?P<ct_id>\d+)/studylist/$', flag_question,
        name='flag_question'),
    url(r'^questions/(?P<ct_id>\d+)/respond/$', respond, name='respond'),
    url(r'^questions/(?P<ct_id>\d+)/concept/$', question_concept,
        name='question_concept'),
    url(r'^course/questions/(?P<cq_id>\d+)/$', course_question,
        name='course_question'),
    url(r'^course/questions/(?P<cq_id>\d+)/respond/$', respond_cq,
        name='respond_cq'),
    url(r'^course/questions/(?P<cq_id>\d+)/concept/$', cq_concept,
        name='cq_concept'),
    url(r'^course/lessons/(?P<cl_id>\d+)/$', course_lesson,
        name='course_lesson'),
    url(r'^lessons/(?P<lesson_id>\d+)/concept/$', lesson_concept,
        name='lesson_concept'),
    url(r'^err/(?P<em_id>\d+)/$', error_model, name='error_model'),
    url(r'^err/(?P<em_id>\d+)/remedy/$', remedy_page, name='remedy'),
    url(r'^err/(?P<em_id>\d+)/remediate/$', submit_remedy, name='remediate'),
    url(r'^remediations/(?P<rem_id>\d+)/$', remediation, name='remediation'),
    url(r'^gloss/(?P<glossary_id>\d+)/write/$', glossary_page,
        name='write_glossary'),
    url(r'^gloss/(?P<glossary_id>\d+)/new_term/$', submit_term,
        name='new_term'),

)

