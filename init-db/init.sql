--
-- PostgreSQL database dump
--

-- Dumped from database version 13.21 (Debian 13.21-1.pgdg120+1)
-- Dumped by pg_dump version 14.18 (Ubuntu 14.18-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: food; Type: TABLE; Schema: public; Owner: christ
--

CREATE TABLE public.food (
    id_food integer NOT NULL,
    name character varying(100),
    description text,
    allergy character varying(100),
    main_image_id integer,
    created_at timestamp without time zone
);


ALTER TABLE public.food OWNER TO christ;

--
-- Name: food_id_food_seq; Type: SEQUENCE; Schema: public; Owner: christ
--

CREATE SEQUENCE public.food_id_food_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.food_id_food_seq OWNER TO christ;

--
-- Name: food_id_food_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: christ
--

ALTER SEQUENCE public.food_id_food_seq OWNED BY public.food.id_food;


--
-- Name: food_image; Type: TABLE; Schema: public; Owner: christ
--

CREATE TABLE public.food_image (
    food_id integer NOT NULL,
    image_id integer NOT NULL,
    is_primary boolean
);


ALTER TABLE public.food_image OWNER TO christ;

--
-- Name: food_ingredient; Type: TABLE; Schema: public; Owner: christ
--

CREATE TABLE public.food_ingredient (
    food_id integer NOT NULL,
    ingredient_id integer NOT NULL,
    quantity double precision
);


ALTER TABLE public.food_ingredient OWNER TO christ;

--
-- Name: image; Type: TABLE; Schema: public; Owner: christ
--

CREATE TABLE public.image (
    id_img integer NOT NULL,
    url character varying(255) NOT NULL,
    created_at timestamp without time zone
);


ALTER TABLE public.image OWNER TO christ;

--
-- Name: image_id_img_seq; Type: SEQUENCE; Schema: public; Owner: christ
--

CREATE SEQUENCE public.image_id_img_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.image_id_img_seq OWNER TO christ;

--
-- Name: image_id_img_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: christ
--

ALTER SEQUENCE public.image_id_img_seq OWNED BY public.image.id_img;


--
-- Name: ingredient; Type: TABLE; Schema: public; Owner: christ
--

CREATE TABLE public.ingredient (
    id_ing integer NOT NULL,
    name character varying(100) NOT NULL,
    created_at timestamp without time zone
);


ALTER TABLE public.ingredient OWNER TO christ;

--
-- Name: ingredient_id_ing_seq; Type: SEQUENCE; Schema: public; Owner: christ
--

CREATE SEQUENCE public.ingredient_id_ing_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingredient_id_ing_seq OWNER TO christ;

--
-- Name: ingredient_id_ing_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: christ
--

ALTER SEQUENCE public.ingredient_id_ing_seq OWNED BY public.ingredient.id_ing;


--
-- Name: person; Type: TABLE; Schema: public; Owner: christ
--

CREATE TABLE public.person (
    id_per integer NOT NULL,
    name character varying(100) NOT NULL,
    age integer,
    created_at timestamp without time zone
);


ALTER TABLE public.person OWNER TO christ;

--
-- Name: person_food; Type: TABLE; Schema: public; Owner: christ
--

CREATE TABLE public.person_food (
    person_id integer NOT NULL,
    food_id integer NOT NULL,
    consumption_date timestamp without time zone,
    quantity integer
);


ALTER TABLE public.person_food OWNER TO christ;

--
-- Name: person_id_per_seq; Type: SEQUENCE; Schema: public; Owner: christ
--

CREATE SEQUENCE public.person_id_per_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.person_id_per_seq OWNER TO christ;

--
-- Name: person_id_per_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: christ
--

ALTER SEQUENCE public.person_id_per_seq OWNED BY public.person.id_per;


--
-- Name: food id_food; Type: DEFAULT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.food ALTER COLUMN id_food SET DEFAULT nextval('public.food_id_food_seq'::regclass);


--
-- Name: image id_img; Type: DEFAULT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.image ALTER COLUMN id_img SET DEFAULT nextval('public.image_id_img_seq'::regclass);


--
-- Name: ingredient id_ing; Type: DEFAULT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.ingredient ALTER COLUMN id_ing SET DEFAULT nextval('public.ingredient_id_ing_seq'::regclass);


--
-- Name: person id_per; Type: DEFAULT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.person ALTER COLUMN id_per SET DEFAULT nextval('public.person_id_per_seq'::regclass);


--
-- Data for Name: food; Type: TABLE DATA; Schema: public; Owner: christ
--

COPY public.food (id_food, name, description, allergy, main_image_id, created_at) FROM stdin;
1	Sushi	Riz vinaigré garni de poisson cru, fruits de mer ou légumes.	Poisson, soja	1	2025-06-11 15:42:57.472676
2	Ramen	Soupe de nouilles dans un bouillon à base de viande ou poisson.	Blé, œuf, soja	2	2025-06-11 15:42:57.474368
3	Tempura	Beignets légers de crevettes et légumes.	Crevettes, blé	3	2025-06-11 15:42:57.475547
4	Okonomiyaki	Crêpe salée à base de chou et de viande ou fruits de mer.	Blé, œuf, fruits de mer	4	2025-06-11 15:42:57.476734
5	Tonkatsu	Côtelette de porc panée et frite, servie avec du chou.	Porc, blé, œuf	5	2025-06-11 15:42:57.477891
\.


--
-- Data for Name: food_image; Type: TABLE DATA; Schema: public; Owner: christ
--

COPY public.food_image (food_id, image_id, is_primary) FROM stdin;
1	1	t
2	2	t
3	3	t
4	4	t
5	5	t
\.


--
-- Data for Name: food_ingredient; Type: TABLE DATA; Schema: public; Owner: christ
--

COPY public.food_ingredient (food_id, ingredient_id, quantity) FROM stdin;
1	1	100
1	2	50
2	3	150
2	4	200
3	5	100
4	6	120
4	8	100
4	9	50
4	10	70
5	7	150
5	6	80
5	8	50
5	9	40
\.


--
-- Data for Name: image; Type: TABLE DATA; Schema: public; Owner: christ
--

COPY public.image (id_img, url, created_at) FROM stdin;
1	https://example.com/sushi.jpg	2025-06-11 15:42:57.462392
2	https://example.com/ramen.jpg	2025-06-11 15:42:57.464228
3	https://example.com/tempura.jpg	2025-06-11 15:42:57.465413
4	https://example.com/okonomiyaki.jpg	2025-06-11 15:42:57.466574
5	https://example.com/tonkatsu.jpg	2025-06-11 15:42:57.467744
\.


--
-- Data for Name: ingredient; Type: TABLE DATA; Schema: public; Owner: christ
--

COPY public.ingredient (id_ing, name, created_at) FROM stdin;
1	Riz	2025-06-11 15:42:57.481606
2	Poisson cru	2025-06-11 15:42:57.483045
3	Nouilles	2025-06-11 15:42:57.48412
4	Bouillon	2025-06-11 15:42:57.485201
5	Crevettes	2025-06-11 15:42:57.486278
6	Chou	2025-06-11 15:42:57.48735
7	Porc	2025-06-11 15:42:57.488431
8	Farine de blé	2025-06-11 15:42:57.489488
9	Oeuf	2025-06-11 15:42:57.490683
10	Fruits de mer	2025-06-11 15:42:57.492031
\.


--
-- Data for Name: person; Type: TABLE DATA; Schema: public; Owner: christ
--

COPY public.person (id_per, name, age, created_at) FROM stdin;
1	Akira Tanaka	28	2025-06-11 15:42:57.524183
2	Yuki Sato	34	2025-06-11 15:42:57.525657
3	Hiroshi Yamamoto	42	2025-06-11 15:42:57.527014
4	Sakura Watanabe	26	2025-06-11 15:42:57.528292
5	Kenji Ito	31	2025-06-11 15:42:57.529505
6	Mei Lin Chen	29	2025-06-11 15:42:57.530672
7	Taro Suzuki	45	2025-06-11 15:42:57.531862
8	Yuki Takahashi	23	2025-06-11 15:42:57.533096
9	Hana Kobayashi	37	2025-06-11 15:42:57.534232
10	Ryu Nakamura	33	2025-06-11 15:42:57.535406
11	Emma Johnson	27	2025-06-11 15:42:57.53659
12	Pierre Dubois	35	2025-06-11 15:42:57.537747
13	Maria Garcia	24	2025-06-11 15:42:57.538947
14	Hans Mueller	41	2025-06-11 15:42:57.540092
15	Anna Kowalski	29	2025-06-11 15:42:57.541449
16	Luigi Rossi	38	2025-06-11 15:42:57.542667
17	Sofia Petrov	32	2025-06-11 15:42:57.54394
18	João Silva	26	2025-06-11 15:42:57.54516
19	Raj Patel	30	2025-06-11 15:42:57.546432
20	Ahmed Hassan	36	2025-06-11 15:42:57.547636
21	Fatima Al-Rashid	25	2025-06-11 15:42:57.548891
22	David Smith	43	2025-06-11 15:42:57.55009
23	Sarah Wilson	31	2025-06-11 15:42:57.551363
24	Michael Brown	28	2025-06-11 15:42:57.552522
25	Jennifer Davis	33	2025-06-11 15:42:57.553798
26	Robert Miller	39	2025-06-11 15:42:57.555056
27	Lisa Anderson	27	2025-06-11 15:42:57.556346
28	James Taylor	35	2025-06-11 15:42:57.557487
29	Mary Johnson	29	2025-06-11 15:42:57.558684
30	Christopher Lee	32	2025-06-11 15:42:57.559917
31	Patricia Williams	26	2025-06-11 15:42:57.561105
32	Daniel Jones	40	2025-06-11 15:42:57.562354
33	Barbara Garcia	34	2025-06-11 15:42:57.563603
34	Matthew Rodriguez	31	2025-06-11 15:42:57.564892
35	Elizabeth Martinez	28	2025-06-11 15:42:57.566143
36	Anthony Hernandez	37	2025-06-11 15:42:57.567444
37	Helen Lopez	25	2025-06-11 15:42:57.568629
38	Mark Gonzalez	42	2025-06-11 15:42:57.569851
39	Donna Wilson	30	2025-06-11 15:42:57.571039
40	Steven Anderson	33	2025-06-11 15:42:57.572282
41	Carol Thomas	29	2025-06-11 15:42:57.573537
42	Joshua Jackson	36	2025-06-11 15:42:57.574824
43	Sharon White	27	2025-06-11 15:42:57.576065
44	Kenneth Harris	41	2025-06-11 15:42:57.57743
45	Michelle Martin	32	2025-06-11 15:42:57.578676
46	Kevin Thompson	28	2025-06-11 15:42:57.579965
47	Nancy Garcia	35	2025-06-11 15:42:57.581229
48	Brian Martinez	31	2025-06-11 15:42:57.582504
49	Betty Robinson	26	2025-06-11 15:42:57.583763
50	Edward Clark	39	2025-06-11 15:42:57.585123
51	Dorothy Rodriguez	33	2025-06-11 15:42:57.586394
52	Ronald Lewis	30	2025-06-11 15:42:57.587672
53	Lisa Lee	28	2025-06-11 15:42:57.58898
54	Jason Walker	37	2025-06-11 15:42:57.590257
55	Karen Hall	25	2025-06-11 15:42:57.591499
56	Thomas Allen	42	2025-06-11 15:42:57.592782
57	Susan Young	34	2025-06-11 15:42:57.594069
58	Charles Hernandez	31	2025-06-11 15:42:57.595393
59	Jessica King	29	2025-06-11 15:42:57.596582
60	Christopher Wright	36	2025-06-11 15:42:57.597852
61	Sarah Lopez	27	2025-06-11 15:42:57.599107
62	Daniel Hill	40	2025-06-11 15:42:57.600455
63	Nancy Scott	32	2025-06-11 15:42:57.601687
64	Matthew Green	28	2025-06-11 15:42:57.602929
65	Laura Adams	35	2025-06-11 15:42:57.604186
66	Anthony Baker	31	2025-06-11 15:42:57.605483
67	Cynthia Gonzalez	26	2025-06-11 15:42:57.606688
68	Mark Nelson	38	2025-06-11 15:42:57.607895
69	Amy Carter	29	2025-06-11 15:42:57.609113
70	Donald Mitchell	33	2025-06-11 15:42:57.610416
71	Melissa Perez	30	2025-06-11 15:42:57.611592
72	Paul Roberts	37	2025-06-11 15:42:57.612857
73	Kimberly Turner	25	2025-06-11 15:42:57.614091
74	Joshua Phillips	41	2025-06-11 15:42:57.615447
75	Mary Campbell	32	2025-06-11 15:42:57.616698
76	Andrew Parker	28	2025-06-11 15:42:57.617933
77	Lisa Evans	34	2025-06-11 15:42:57.619296
78	Kenneth Edwards	31	2025-06-11 15:42:57.620483
79	Michelle Collins	27	2025-06-11 15:42:57.621741
80	Brian Stewart	39	2025-06-11 15:42:57.623009
81	Carol Sanchez	30	2025-06-11 15:42:57.624311
82	Edward Morris	33	2025-06-11 15:42:57.625603
83	Sharon Rogers	28	2025-06-11 15:42:57.626897
84	Steven Reed	36	2025-06-11 15:42:57.628067
85	Helen Cook	25	2025-06-11 15:42:57.62939
86	Jason Morgan	42	2025-06-11 15:42:57.630608
87	Karen Bailey	29	2025-06-11 15:42:57.631892
88	Thomas Rivera	35	2025-06-11 15:42:57.633126
89	Donna Cooper	31	2025-06-11 15:42:57.634396
90	Christopher Richardson	26	2025-06-11 15:42:57.635603
91	Nancy Cox	38	2025-06-11 15:42:57.63688
92	Daniel Howard	30	2025-06-11 15:42:57.638082
93	Susan Ward	33	2025-06-11 15:42:57.639324
94	Matthew Torres	28	2025-06-11 15:42:57.640619
95	Patricia Peterson	37	2025-06-11 15:42:57.6419
96	Anthony Gray	25	2025-06-11 15:42:57.643098
97	Jennifer Ramirez	41	2025-06-11 15:42:57.644506
98	Mark James	32	2025-06-11 15:42:57.645695
99	Linda Watson	29	2025-06-11 15:42:57.64689
100	David Brooks	34	2025-06-11 15:42:57.648086
101	Barbara Kelly	31	2025-06-11 15:42:57.64935
102	Robert Sanders	27	2025-06-11 15:42:57.650512
103	Elizabeth Price	39	2025-06-11 15:42:57.651765
104	Michael Bennett	30	2025-06-11 15:42:57.653035
105	Mary Wood	33	2025-06-11 15:42:57.654366
\.


--
-- Data for Name: person_food; Type: TABLE DATA; Schema: public; Owner: christ
--

COPY public.person_food (person_id, food_id, consumption_date, quantity) FROM stdin;
1	3	2025-06-11 16:42:57.658388	2
2	4	2025-06-11 16:42:57.660359	3
3	2	2025-06-11 16:42:57.661877	3
3	5	2025-06-11 16:42:57.663222	3
4	2	2025-06-11 16:42:57.664566	2
4	4	2025-06-11 16:42:57.665755	2
4	1	2025-06-11 16:42:57.666983	3
5	4	2025-06-11 16:42:57.668126	2
5	5	2025-06-11 16:42:57.669256	3
5	1	2025-06-11 16:42:57.670364	1
6	1	2025-06-11 16:42:57.671435	1
7	1	2025-06-11 16:42:57.672502	2
8	1	2025-06-11 16:42:57.673549	2
8	5	2025-06-11 16:42:57.674623	3
8	3	2025-06-11 16:42:57.675708	3
9	2	2025-06-11 16:42:57.67677	3
9	1	2025-06-11 16:42:57.677847	1
9	4	2025-06-11 16:42:57.67915	2
10	3	2025-06-11 16:42:57.680362	3
11	4	2025-06-11 16:42:57.68143	1
12	5	2025-06-11 16:42:57.682482	3
12	4	2025-06-11 16:42:57.683497	3
13	2	2025-06-11 16:42:57.68455	3
13	3	2025-06-11 16:42:57.685596	3
14	3	2025-06-11 16:42:57.686611	1
15	4	2025-06-11 16:42:57.687659	1
15	5	2025-06-11 16:42:57.688682	1
15	2	2025-06-11 16:42:57.689709	2
16	5	2025-06-11 16:42:57.69075	3
16	2	2025-06-11 16:42:57.69179	1
17	2	2025-06-11 16:42:57.69287	1
17	4	2025-06-11 16:42:57.693923	1
18	5	2025-06-11 16:42:57.695017	3
19	3	2025-06-11 16:42:57.69612	1
19	5	2025-06-11 16:42:57.697178	2
19	2	2025-06-11 16:42:57.698233	2
20	2	2025-06-11 16:42:57.699324	2
20	1	2025-06-11 16:42:57.700403	1
21	5	2025-06-11 16:42:57.701554	3
21	2	2025-06-11 16:42:57.702664	2
22	5	2025-06-11 16:42:57.703763	2
22	1	2025-06-11 16:42:57.704882	3
23	5	2025-06-11 16:42:57.706034	1
23	4	2025-06-11 16:42:57.707244	2
24	4	2025-06-11 16:42:57.708327	3
25	3	2025-06-11 16:42:57.709496	3
26	1	2025-06-11 16:42:57.710606	1
27	3	2025-06-11 16:42:57.711685	3
27	1	2025-06-11 16:42:57.712751	3
27	5	2025-06-11 16:42:57.713875	3
28	2	2025-06-11 16:42:57.714998	1
29	2	2025-06-11 16:42:57.716161	1
29	3	2025-06-11 16:42:57.717312	1
29	1	2025-06-11 16:42:57.718748	3
30	1	2025-06-11 16:42:57.720013	1
30	5	2025-06-11 16:42:57.72128	1
30	3	2025-06-11 16:42:57.722514	2
31	5	2025-06-11 16:42:57.723766	2
31	4	2025-06-11 16:42:57.724969	3
31	2	2025-06-11 16:42:57.726179	2
32	3	2025-06-11 16:42:57.727438	3
32	5	2025-06-11 16:42:57.728682	3
33	4	2025-06-11 16:42:57.729914	1
34	5	2025-06-11 16:42:57.731231	3
34	4	2025-06-11 16:42:57.732492	1
35	2	2025-06-11 16:42:57.733763	3
35	1	2025-06-11 16:42:57.734997	3
36	3	2025-06-11 16:42:57.736268	3
37	4	2025-06-11 16:42:57.737498	3
37	1	2025-06-11 16:42:57.738731	1
37	3	2025-06-11 16:42:57.739942	2
38	2	2025-06-11 16:42:57.741246	2
38	1	2025-06-11 16:42:57.742466	3
38	5	2025-06-11 16:42:57.743725	2
39	2	2025-06-11 16:42:57.744991	3
40	4	2025-06-11 16:42:57.746288	2
40	2	2025-06-11 16:42:57.747535	2
41	1	2025-06-11 16:42:57.748752	2
41	4	2025-06-11 16:42:57.750049	3
42	5	2025-06-11 16:42:57.751301	1
43	3	2025-06-11 16:42:57.752532	2
44	2	2025-06-11 16:42:57.753795	1
44	1	2025-06-11 16:42:57.754994	3
45	5	2025-06-11 16:42:57.756271	1
45	3	2025-06-11 16:42:57.757621	2
45	4	2025-06-11 16:42:57.758816	3
46	3	2025-06-11 16:42:57.759936	1
46	5	2025-06-11 16:42:57.761139	3
47	4	2025-06-11 16:42:57.762292	2
47	5	2025-06-11 16:42:57.76343	3
48	2	2025-06-11 16:42:57.764624	2
49	1	2025-06-11 16:42:57.76578	1
49	2	2025-06-11 16:42:57.766944	2
49	5	2025-06-11 16:42:57.768126	2
50	3	2025-06-11 16:42:57.76932	1
50	1	2025-06-11 16:42:57.770452	1
50	5	2025-06-11 16:42:57.7716	3
51	1	2025-06-11 16:42:57.772719	1
51	5	2025-06-11 16:42:57.773849	2
51	3	2025-06-11 16:42:57.774971	3
52	3	2025-06-11 16:42:57.776236	3
52	4	2025-06-11 16:42:57.777536	1
53	5	2025-06-11 16:42:57.778775	1
54	5	2025-06-11 16:42:57.780166	1
54	2	2025-06-11 16:42:57.781727	1
55	1	2025-06-11 16:42:57.783356	1
56	2	2025-06-11 16:42:57.784729	1
56	4	2025-06-11 16:42:57.78615	2
57	3	2025-06-11 16:42:57.787637	3
57	4	2025-06-11 16:42:57.788979	3
57	1	2025-06-11 16:42:57.79012	1
58	3	2025-06-11 16:42:57.791266	3
58	4	2025-06-11 16:42:57.792398	2
58	5	2025-06-11 16:42:57.793539	3
59	3	2025-06-11 16:42:57.794681	3
59	5	2025-06-11 16:42:57.795839	1
60	4	2025-06-11 16:42:57.796944	2
60	5	2025-06-11 16:42:57.798043	2
61	5	2025-06-11 16:42:57.799119	3
61	3	2025-06-11 16:42:57.800298	2
61	2	2025-06-11 16:42:57.801385	1
62	5	2025-06-11 16:42:57.80246	2
62	1	2025-06-11 16:42:57.80358	2
63	1	2025-06-11 16:42:57.804685	2
64	5	2025-06-11 16:42:57.805786	3
64	2	2025-06-11 16:42:57.806912	1
65	5	2025-06-11 16:42:57.808076	3
65	3	2025-06-11 16:42:57.809223	3
65	4	2025-06-11 16:42:57.810316	1
66	4	2025-06-11 16:42:57.811467	2
66	2	2025-06-11 16:42:57.812562	2
66	5	2025-06-11 16:42:57.813648	3
67	1	2025-06-11 16:42:57.81471	2
67	4	2025-06-11 16:42:57.815822	1
67	5	2025-06-11 16:42:57.816902	1
68	4	2025-06-11 16:42:57.818058	3
68	1	2025-06-11 16:42:57.81923	1
69	1	2025-06-11 16:42:57.820334	2
69	5	2025-06-11 16:42:57.82144	2
69	3	2025-06-11 16:42:57.822578	1
70	5	2025-06-11 16:42:57.82369	3
70	2	2025-06-11 16:42:57.824748	1
70	4	2025-06-11 16:42:57.825997	3
71	3	2025-06-11 16:42:57.827238	3
71	2	2025-06-11 16:42:57.828435	2
72	5	2025-06-11 16:42:57.829575	2
72	3	2025-06-11 16:42:57.830734	2
73	1	2025-06-11 16:42:57.831918	2
74	4	2025-06-11 16:42:57.833135	1
75	2	2025-06-11 16:42:57.834316	2
75	3	2025-06-11 16:42:57.835409	3
75	1	2025-06-11 16:42:57.836575	1
76	4	2025-06-11 16:42:57.837695	3
76	1	2025-06-11 16:42:57.838797	3
76	2	2025-06-11 16:42:57.839872	3
77	3	2025-06-11 16:42:57.840939	1
77	2	2025-06-11 16:42:57.842093	1
78	5	2025-06-11 16:42:57.843281	1
78	2	2025-06-11 16:42:57.844489	2
79	5	2025-06-11 16:42:57.845651	1
80	5	2025-06-11 16:42:57.846739	3
81	5	2025-06-11 16:42:57.847799	3
82	3	2025-06-11 16:42:57.848857	1
83	3	2025-06-11 16:42:57.849942	3
83	4	2025-06-11 16:42:57.85116	1
83	1	2025-06-11 16:42:57.852333	2
84	5	2025-06-11 16:42:57.853421	1
84	1	2025-06-11 16:42:57.85458	2
84	2	2025-06-11 16:42:57.855665	2
85	3	2025-06-11 16:42:57.857131	1
85	2	2025-06-11 16:42:57.858451	2
86	5	2025-06-11 16:42:57.859558	3
87	1	2025-06-11 16:42:57.860591	1
87	2	2025-06-11 16:42:57.861839	3
87	3	2025-06-11 16:42:57.863101	1
88	3	2025-06-11 16:42:57.864293	1
88	5	2025-06-11 16:42:57.865472	3
88	1	2025-06-11 16:42:57.866561	2
89	2	2025-06-11 16:42:57.868072	2
90	4	2025-06-11 16:42:57.8695	2
90	5	2025-06-11 16:42:57.870668	1
91	5	2025-06-11 16:42:57.871752	3
92	1	2025-06-11 16:42:57.872871	1
92	3	2025-06-11 16:42:57.874001	3
93	4	2025-06-11 16:42:57.875127	1
94	2	2025-06-11 16:42:57.876287	2
95	1	2025-06-11 16:42:57.877402	1
95	5	2025-06-11 16:42:57.87852	3
96	1	2025-06-11 16:42:57.879683	3
96	2	2025-06-11 16:42:57.880886	3
96	4	2025-06-11 16:42:57.882032	1
97	5	2025-06-11 16:42:57.883153	1
97	1	2025-06-11 16:42:57.884202	2
97	4	2025-06-11 16:42:57.885265	2
98	4	2025-06-11 16:42:57.886362	3
99	4	2025-06-11 16:42:57.887408	2
100	1	2025-06-11 16:42:57.888492	3
100	2	2025-06-11 16:42:57.889543	1
100	5	2025-06-11 16:42:57.890628	2
\.


--
-- Name: food_id_food_seq; Type: SEQUENCE SET; Schema: public; Owner: christ
--

SELECT pg_catalog.setval('public.food_id_food_seq', 5, true);


--
-- Name: image_id_img_seq; Type: SEQUENCE SET; Schema: public; Owner: christ
--

SELECT pg_catalog.setval('public.image_id_img_seq', 5, true);


--
-- Name: ingredient_id_ing_seq; Type: SEQUENCE SET; Schema: public; Owner: christ
--

SELECT pg_catalog.setval('public.ingredient_id_ing_seq', 10, true);


--
-- Name: person_id_per_seq; Type: SEQUENCE SET; Schema: public; Owner: christ
--

SELECT pg_catalog.setval('public.person_id_per_seq', 105, true);


--
-- Name: food_image food_image_pkey; Type: CONSTRAINT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.food_image
    ADD CONSTRAINT food_image_pkey PRIMARY KEY (food_id, image_id);


--
-- Name: food_ingredient food_ingredient_pkey; Type: CONSTRAINT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.food_ingredient
    ADD CONSTRAINT food_ingredient_pkey PRIMARY KEY (food_id, ingredient_id);


--
-- Name: food food_pkey; Type: CONSTRAINT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.food
    ADD CONSTRAINT food_pkey PRIMARY KEY (id_food);


--
-- Name: image image_pkey; Type: CONSTRAINT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.image
    ADD CONSTRAINT image_pkey PRIMARY KEY (id_img);


--
-- Name: ingredient ingredient_pkey; Type: CONSTRAINT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.ingredient
    ADD CONSTRAINT ingredient_pkey PRIMARY KEY (id_ing);


--
-- Name: person_food person_food_pkey; Type: CONSTRAINT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.person_food
    ADD CONSTRAINT person_food_pkey PRIMARY KEY (person_id, food_id);


--
-- Name: person person_pkey; Type: CONSTRAINT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_pkey PRIMARY KEY (id_per);


--
-- Name: food_image food_image_food_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.food_image
    ADD CONSTRAINT food_image_food_id_fkey FOREIGN KEY (food_id) REFERENCES public.food(id_food);


--
-- Name: food_image food_image_image_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.food_image
    ADD CONSTRAINT food_image_image_id_fkey FOREIGN KEY (image_id) REFERENCES public.image(id_img);


--
-- Name: food_ingredient food_ingredient_food_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.food_ingredient
    ADD CONSTRAINT food_ingredient_food_id_fkey FOREIGN KEY (food_id) REFERENCES public.food(id_food);


--
-- Name: food_ingredient food_ingredient_ingredient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.food_ingredient
    ADD CONSTRAINT food_ingredient_ingredient_id_fkey FOREIGN KEY (ingredient_id) REFERENCES public.ingredient(id_ing);


--
-- Name: food food_main_image_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.food
    ADD CONSTRAINT food_main_image_id_fkey FOREIGN KEY (main_image_id) REFERENCES public.image(id_img);


--
-- Name: person_food person_food_food_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.person_food
    ADD CONSTRAINT person_food_food_id_fkey FOREIGN KEY (food_id) REFERENCES public.food(id_food);


--
-- Name: person_food person_food_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: christ
--

ALTER TABLE ONLY public.person_food
    ADD CONSTRAINT person_food_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.person(id_per);


--
-- PostgreSQL database dump complete
--

