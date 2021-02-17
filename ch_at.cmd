!#####################!
!##      {{ rsite }}     ##!
!#####################!

{% for cell in cells %}
RLSTC:CELL={{cell}},STATE=HALTED;
{% endfor %}

{% for tg in tgs %}
RXBLI:MO=RXSTG-{{tg}},FORCE;
{% endfor %}

@X Release
@T 15
@S Connect

{% for tg in tgs %}
RXESE:MO=RXSTG-{{tg}};
{% endfor %}

@X Release
@T 15
@S Connect

{% for tg in tgs %}
RXMOC:MO=RXSAT-{{tg}},MCLTDL=5,MCLTUL=5,SIGDEL=NORMAL,SAPI=0,DSCPDL=46,DSCPUL=46;
RXMOC:MO=RXSAT-{{tg}},MCLTDL=5,MCLTUL=5,SIGDEL=NORMAL,SAPI=62,DSCPDL=46,DSCPUL=46;
RXMOC:MO=RXSAT-{{tg}},MCLTDL=5,MCLTUL=5,SIGDEL=NORMAL,SAPI=10,DSCPDL=36,DSCPUL=36;
RXMOC:MO=RXSAT-{{tg}},MCLTDL=5,MCLTUL=5,SIGDEL=NORMAL,SAPI=11,DSCPDL=36,DSCPUL=36;
RXMOC:MO=RXSAT-{{tg}},MCLTDL=5,MCLTUL=5,SIGDEL=NORMAL,SAPI=12,DSCPDL=18,DSCPUL=18;
{% endfor %}

{% for tg in tgs %}
RXESI:MO=RXSTG-{{tg}};
RXBLE:MO=RXSTG-{{tg}};
{% endfor %}


@X Release
@T 15
@S Connect

{% for cell in cells %}
RLSTC:CELL={{cell}},STATE=ACTIVE;
{% endfor %}


