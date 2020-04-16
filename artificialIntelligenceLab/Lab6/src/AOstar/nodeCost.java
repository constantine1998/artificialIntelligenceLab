package AOstar;

public class nodeCost {

	public static int calCost(Node s) {
		if(s.mSize == 2) return 0;
		if(s.mSize == 3) return s.nxm.get(0) * s.nxm.get(1) * s.nxm.get(2);
		if(s.IsOrNode) return calCost(s.children.get(s.marker));
		else return calCost(s.children.get(0)) + calCost(s.children.get(1)) + (s.children.get(0).nxm.get(0)*s.children.get(1).nxm.get(0)*s.children.get(1).nxm.get(s.children.get(1).mSize-1));
	}
}
