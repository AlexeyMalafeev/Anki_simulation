# Anki_simulation

Anki scheduling simulation

## Functionality

1. Simulate related cards (no two cards are shown on the same day; if 
   multiple cards are scheduled for one day, one is chosen at random).
   
For example,
   

    simulate(n_cards=25,
            n_days=150,
            ease=2.5,
            mult=1.25,
            first_interval=3)

might output:

    cards: 10, days: 60, ease: 2.5, mult: 1.25, first_interval: 3
    first occurrences:
    {0: 27, 1: 1, 2: 2, 3: 3, 4: 7, 5: 8, 6: 9, 7: 13, 8: 18, 9: 19, 10: 25}
    
    schedule:
    1: 1	2: 2	3: 3	4: 1	5: 2	6: 3	7: 4	8: 5	9: 6	10: 4	11: 5	12: 6	13: 7	14: 1	15: 2	16: 7	17: 3	18: 8	19: 9	20: 4	21: 5	22: 9	23: 8	24: 6	25: 10	26: 7	27: 0	28: 10	29: 0	30: 0	31: 0	32: 9	33: 0	34: 0	35: 8	36: 0	37: 0	38: 10	39: 0	40: 0	41: 0	42: 0	43: 0	44: 1	45: 2	46: 0	47: 0	48: 3	49: 0	50: 4	51: 5	52: 0	53: 0	54: 0	55: 0	56: 7	57: 6	58: 0	59: 0	60: 0
    
    intervals:
    {1: 286.102294921875,
     2: 286.102294921875,
     3: 295.867919921875,
     4: 286.102294921875,
     5: 286.102294921875,
     6: 308.758544921875,
     7: 286.102294921875,
     8: 111.083984375,
     9: 91.552734375,
     10: 91.552734375}


2. Compare different Anki settings and see how they affect card intervals. 

For example:

    compare_intervals()
    
    intervals for ease: 2.5, mult: 1.0, first_interval: 1
    1	3	7	16	40	98	245	611	1526	3815
    average intervals for ease: 2.5, mult: 1.0, first_interval: 1, lapse_prob: 0.1, after_lapse_coef: 0.6, n_sim: 10
    1	2	6	14	33	75	186	462	1031	2265
    
    intervals for ease: 2.5, mult: 1.25, first_interval: 3
    3	10	30	92	287	895	2794	8732	27285	85266
    average intervals for ease: 2.5, mult: 1.25, first_interval: 3, lapse_prob: 0.1, after_lapse_coef: 0.6, n_sim: 10
    3	9	24	75	235	732	2057	5677	15423	47744
    
    intervals for ease: 2.5, mult: 2.0, first_interval: 3
    3	15	75	375	1875	9375	46875	234375	1171875	5859375
    average intervals for ease: 2.5, mult: 2.0, first_interval: 3, lapse_prob: 0.1, after_lapse_coef: 0.6, n_sim: 10
    3	15	68	342	1525	6789	33850	148034	634062	2635355
    
    intervals for ease: 2.5, mult: 2.0, first_interval: 30
    30	150	750	3750	18750	93750	468750	2343750	11718750	58593750
    average intervals for ease: 2.5, mult: 2.0, first_interval: 30, lapse_prob: 0.1, after_lapse_coef: 0.6, n_sim: 10
    30	150	750	3420	15432	60487	300741	1495909	7443682	31459176
    
    intervals for ease: 3.0, mult: 1.0, first_interval: 3
    3	9	27	81	243	729	2187	6561	19683	59049
    average intervals for ease: 3.0, mult: 1.0, first_interval: 3, lapse_prob: 0.1, after_lapse_coef: 0.6, n_sim: 10
    3	8	23	68	184	479	1253	3726	10816	27505
    
    intervals for ease: 3.15, mult: 1.0, first_interval: 3
    3	10	30	94	296	931	2931	9232	29081	91605
    average intervals for ease: 3.15, mult: 1.0, first_interval: 3, lapse_prob: 0.1, after_lapse_coef: 0.6, n_sim: 10
    3	9	25	63	174	543	1180	3550	8286	25410
    
    intervals for ease: 3.25, mult: 1.0, first_interval: 3
    3	10	32	103	335	1088	3536	11490	37342	121359
    average intervals for ease: 3.25, mult: 1.0, first_interval: 3, lapse_prob: 0.1, after_lapse_coef: 0.6, n_sim: 10
    3	10	27	76	247	799	2299	7417	23594	76197
    
    intervals for ease: 3.5, mult: 1.0, first_interval: 3
    3	11	37	129	451	1576	5515	19302	67557	236447
    average intervals for ease: 3.5, mult: 1.0, first_interval: 3, lapse_prob: 0.1, after_lapse_coef: 0.6, n_sim: 10
    3	10	34	118	338	917	3182	10585	36839	106196

