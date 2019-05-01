#include <iostream>
#include <vector>
#include <time.h>
#include <map>
#include <set>
#include <stdlib.h>
// #include <unordered_map>

using namespace std;

struct Point{
	int x;
	int y;
	Point(): x(0), y(0) {}
	Point(int a, int b): x(a), y(b) {} 
}; 

// #define INT_MAX 2147483647
// #define INT_MIN (- INT_MAX - 1)

class Solution{
public:
	int maxPoints(vector<Point> &points){

		
		if (points.size() == 0)	return 0;
		if (points.size() <= 2) return points.size();
		
		int max_value = 0;
		map<double, int> slopeMap;

		for (int i = 0; i < points.size() - 1; i++){
			int sameCount = 1;
			slopeMap.clear();
			slopeMap[INT_MIN] = 0;
			for (int j = i + 1; j < points.size(); j++){
				int delta_x = points[i].x - points[j].x;
				int delta_y = points[i].y - points[j].y;

				if (delta_x == 0 && delta_y == 0){
					sameCount++;
				}
				else{
					double slope = INT_MAX;
					if (delta_x != 0){
						slope = 1.0 * delta_y / delta_x;
					}
					slopeMap[slope]++;
				}
			}

			map<double, int>::iterator it;
			for (it = slopeMap.begin(); it != slopeMap.end(); it++){
				if (max_value < (it->second + sameCount)){
					max_value = it->second + sameCount;
					// cout << sameCount << endl;
				}
			}
		}
		
		return max_value;
	}	
};

void generatePoints(vector<Point> &points, int n){
	srand(time(0));
	Point p;
	
	for (int i = 0; i < n; i++){
		p.x = rand() % 1;
		p.y = rand() % 1;
		points.push_back(p);
	}
}

void printPoints(vector<Point> & points){
	for (int i = 0; i < points.size(); i++){
		cout << "(" << points[i].x << "," << points[i].y << ")";
	}
	cout << endl;
}

int main(int argc, char** argv){
	// int n = 20;
	// if (argc > 1){
	// 	n = atoi(argv.[1]);
	// }

	vector<Point> points;
	// generatePoints(points, n);
	// printPoints(points);

	Point p1;
	p1.x = 3;
	p1.y = 3;

	Point p2;
	p2.x = 3;
	p2.y = 3;

	Point p3;
	p3.x = 3;
	p3.y = 3;

	points.push_back(p1);
	points.push_back(p2);
	points.push_back(p3);

	cout << Solution().maxPoints(points) << endl;
	system("pause");
	return 0;
}