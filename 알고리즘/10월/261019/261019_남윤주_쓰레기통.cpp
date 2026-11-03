/*
쓰레기통 배정

쓰레기통 위치를 찾고, 쓰레기마다 통 3개까지 맨해튼 거리 계산

배정 
모든 쓰레기를 가장 가까운 통에 배정한다. (용량 무시)
3500개를 넘은 통에서, 옮겼을 때 거리가 가장 적게 늘어나는 쓰레기를 자리 있는 통으로 하나씩 보냄

배정된 통까지 가까운 쓰레기부터, 거리가 줄어드는 방향으로 한 칸씩 민다.
*/

void move_trash(int y, int x, int d);

const int N = 1000;
const int CAP = 3500;
const int TMAX = 10000;
const int HMAX = 80000;

int M[N][N];                // 내 지도 
int ty[TMAX], tx[TMAX], tn; // 쓰레기 위치, 개수
int cy[3], cx[3];           // 쓰레기통 위치
int D[TMAX][3];             // 쓰레기 -> 쓰레기통 거리
int asg[TMAX];              // 쓰레기 배정된 통
int load[3];                // 통별 배정 쓰레기 수

int vis[N][N], stamp;       
int pdir[N][N];             
int qy[N * N], qx[N * N];   
int path[N * N];            

int ord[TMAX], done[TMAX], bucket[2 * N + 1];

int dy[4] = { -1, 1, 0, 0 };
int dx[4] = { 0, 0, -1, 1 };

int iabs(int a) {
	return a < 0 ? -a : a;
}


// H[i][j] : 쓰레기통 i의 쓰레기를 j로 바꿀 때 늘어나는 거리 D[t][j] - D[t][i] 의 최소 힙
struct Heap {
	int key[HMAX], val[HMAX], n;

	void clear() {
		n = 0;
	}

	void push(int k, int v) {
		int i = n++;
		while (i > 0 && key[(i - 1) / 2] > k) {
			key[i] = key[(i - 1) / 2];
			val[i] = val[(i - 1) / 2];
			i = (i - 1) / 2;
		}
		key[i] = k;
		val[i] = v;
	}

	void pop() {
		n--;
		int k = key[n];
		int v = val[n];
		int i = 0;
		while (true) {
			int c = 2 * i + 1;
			if (c >= n) break;
			if (c + 1 < n && key[c + 1] < key[c]) c++;
			if (key[c] >= k) break;
			key[i] = key[c];
			val[i] = val[c];
			i = c;
		}
		key[i] = k;
		val[i] = v;
	}
};

Heap H[3][3];


// 쓰레기 t를 통 k에 배정하고 힙에 등록
void place(int t, int k) {
	asg[t] = k;
	for (int j = 0; j < 3; j++) {
		if (j != k) H[k][j].push(D[t][j] - D[t][k], t);
	}
}

// 통 i에서 j로 바꾸기 가장 싼 쓰레기 
int top(int i, int j) {
	while (H[i][j].n > 0 && asg[H[i][j].val[0]] != i) {
		H[i][j].pop();
	}
	if (H[i][j].n == 0) return -1;
	return H[i][j].val[0];
}

// 통 i에서 j로 하나 옮길 때 늘어나는 최소 거리
int cost(int i, int j) {
	int t = top(i, j);
	if (t < 0) return 1 << 29;
	return D[t][j] - D[t][i];
}

// 통 i에서 j로 가장 싼 쓰레기 하나를 옮김
void shift(int i, int j) {
	int t = top(i, j);
	load[i]--;
	load[j]++;
	place(t, j);
}

void assign_all() {
	for (int i = 0; i < 3; i++) {
		load[i] = 0;
		for (int j = 0; j < 3; j++) {
			H[i][j].clear();
		}
	}

	// 1) 가장 가까운 통에 배정 (용량 무시)
	for (int t = 0; t < tn; t++) {
		int k = 0;
		if (D[t][1] < D[t][k]) k = 1;
		if (D[t][2] < D[t][k]) k = 2;
		load[k]++;
		place(t, k);
	}

	// 2) 넘친 통 정리: 직행 o -> j 와 경유 o -> m -> j 중 싼 쪽
	while (true) {
		int o = -1;
		for (int k = 0; k < 3; k++) {
			if (load[k] > CAP) o = k;
		}
		if (o < 0) break;

		int best = 1 << 30, bt = -1, bm = -1;
		for (int j = 0; j < 3; j++) {
			if (j == o || load[j] >= CAP) continue;

			int direct = cost(o, j);
			if (direct < best) {
				best = direct;
				bt = j;
				bm = -1;
			}

			int m = 3 - o - j;
			int relay = cost(o, m) + cost(m, j);
			if (relay < best) {
				best = relay;
				bt = j;
				bm = m;
			}
		}

		if (bm < 0) {
			shift(o, bt);
		}
		else {
			shift(o, bm);
			shift(bm, bt);
		}
	}
}


// 통 k로 가는 쓰레기가 (y, x)에 들어갈 수 있나
bool passable(int y, int x, int k) {
	if (y < 0 || y >= N || x < 0 || x >= N) return false;
	return M[y][x] == 0 || M[y][x] == k + 1;
}

bool step(int t, int d, int k) {
	int y = ty[t];
	int x = tx[t];
	int ny = y + dy[d];
	int nx = x + dx[d];

	move_trash(y, x, d);
	M[y][x] = 0;

	if (M[ny][nx] == k + 1) return true;

	M[ny][nx] = -1;
	ty[t] = ny;
	tx[t] = nx;
	return false;
}

// 막혔을 때 BFS 최단 경로로 운반 (길이 없으면 false)
bool bfs_carry(int t, int k) {
	stamp++;
	int head = 0, tail = 0;
	int sy = ty[t];
	int sx = tx[t];

	qy[tail] = sy;
	qx[tail] = sx;
	tail++;
	vis[sy][sx] = stamp;

	bool found = false;
	while (head < tail) {
		int y = qy[head];
		int x = qx[head];
		head++;

		if (y == cy[k] && x == cx[k]) {
			found = true;
			break;
		}

		for (int d = 0; d < 4; d++) {
			int ny = y + dy[d];
			int nx = x + dx[d];
			if (!passable(ny, nx, k)) continue;
			if (vis[ny][nx] == stamp) continue;

			vis[ny][nx] = stamp;
			pdir[ny][nx] = d;
			qy[tail] = ny;
			qx[tail] = nx;
			tail++;
		}
	}
	if (!found) return false;

	// 통에서 출발점까지 거꾸로 되짚기
	int len = 0;
	int y = cy[k];
	int x = cx[k];
	while (y != sy || x != sx) {
		int d = pdir[y][x];
		path[len++] = d;
		y -= dy[d];
		x -= dx[d];
	}

	for (int i = len - 1; i >= 0; i--) {
		if (step(t, path[i], k)) return true;
	}
	return true;
}

// 쓰레기 t를 통 k까지 (남은 거리가 긴 축 먼저, 둘 다 막히면 BFS)
bool carry(int t, int k) {
	while (true) {
		int y = ty[t];
		int x = tx[t];
		int ddy = cy[k] - y;
		int ddx = cx[k] - x;
		int dv = ddy < 0 ? 0 : 1;
		int dh = ddx < 0 ? 2 : 3;

		int c[2], n = 0;
		if (iabs(ddy) >= iabs(ddx)) {
			if (ddy != 0) c[n++] = dv;
			if (ddx != 0) c[n++] = dh;
		}
		else {
			if (ddx != 0) c[n++] = dh;
			if (ddy != 0) c[n++] = dv;
		}

		int pick = -1;
		for (int i = 0; i < n; i++) {
			if (passable(y + dy[c[i]], x + dx[c[i]], k)) {
				pick = c[i];
				break;
			}
		}

		if (pick < 0) return bfs_carry(t, k);
		if (step(t, pick, k)) return true;
	}
}

// 배정된 통까지 거리가 짧은 쓰레기부터 운반
void run_all() {
	// 거리 기준 계수 정렬
	for (int i = 0; i <= 2 * N; i++) {
		bucket[i] = 0;
	}
	for (int t = 0; t < tn; t++) {
		bucket[D[t][asg[t]]]++;
	}
	for (int i = 1; i <= 2 * N; i++) {
		bucket[i] += bucket[i - 1];
	}
	for (int t = tn - 1; t >= 0; t--) {
		ord[--bucket[D[t][asg[t]]]] = t;
	}
	for (int t = 0; t < tn; t++) {
		done[t] = 0;
	}

	// 막힌 쓰레기는 다음 바퀴에 재시도
	for (int pass = 0; pass < 5; pass++) {
		bool prog = false;
		bool rem = false;

		for (int i = 0; i < tn; i++) {
			int t = ord[i];
			if (done[t]) continue;

			if (carry(t, asg[t])) {
				done[t] = 1;
				prog = true;
			}
			else {
				rem = true;
			}
		}

		if (!rem || !prog) break;
	}
}


void test(int trash_map[1000][1000]) {
	tn = 0;
	for (int y = 0; y < N; y++) {
		for (int x = 0; x < N; x++) {
			int v = trash_map[y][x];
			M[y][x] = v;
			if (v == -1) {
				ty[tn] = y;
				tx[tn] = x;
				tn++;
			}
			else if (v > 0) {
				cy[v - 1] = y;
				cx[v - 1] = x;
			}
		}
	}

	// 거리표
	for (int t = 0; t < tn; t++) {
		for (int k = 0; k < 3; k++) {
			D[t][k] = iabs(ty[t] - cy[k]) + iabs(tx[t] - cx[k]);
		}
	}

	assign_all();
	run_all();
}