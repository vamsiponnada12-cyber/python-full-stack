codegnan_details = {}
codegnan_details['timings'] = ['09AM to 05PM']
codegnan_details['mentors'] = ('saketh','bhanu teja','mallikarjuna','yogitha','rajitha')
codegnan_details['stdnts_pfs'] = ['ranjith','akash','sampath','ramana']

codegnan_details.update({'stdnts_da':['harsha','bablu','ganesh','gagan'],
                         'subjects':{'python','MySQL','aptitude','soft-skills'},
                         'mrng_calsses_timings':['09AM to 01PM'],
                         'aftr_classes_timings':['02PM to 04PM'],
                         'no of courses':['pfs','jfs','da'],
                         'no of batches':[1,2,3,4,5],
                         'daily exams':['monday to saturday'],
                         'daily exam_timings':('07PM to 11PM'),
                         'weekly_exam':['tuesday'],
                         'weekly exam_timings':['11AM to 11PM'],
                         'AI_mock interviews':('sunday','monday'),
                         'interview_timings':['7AM to 12pm']
                         })
codegnan_details['no of batches'].append(6)
codegnan_details['stdnts_pfs'].extend(['bhanu sai','sridhar'])
codegnan_details['stdnts_da'].extend(['gana','krishna'])
codegnan_details['no of courses'].pop('DSA')
print(len(codegnan_details))
print(codegnan_details)































