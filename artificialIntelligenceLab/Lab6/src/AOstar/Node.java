package AOstar;

import java.util.ArrayList;
import java.util.List;

public class Node {
	List<Node> children = new ArrayList<Node>();
	List<Integer> nxm = new ArrayList<Integer>();
	Node parent;
	int marker, dotPosition, index, mSize;
	boolean IsMarkerSet, IsSolved, IsOrNode;
	int hValue = 0;
	
	public Node(List<Integer> data) {
		nxm = data;
		mSize = nxm.size();
		parent = null;
		IsMarkerSet = false;
		hValue += nxm.get(0) * nxm.get(nxm.size()-1);
		if(nxm.size() <= 2) {
			hValue = 0;
		}
		for(int i = 1; i < nxm.size()-1;i += 2) {
			hValue += nxm.get(i) * nxm.get(i+1);
		}
		if(nxm.size() == 3) {
			hValue = nxm.get(0) * nxm.get(1) * nxm.get(2);
		}
		if(nxm.size() <= 3) IsSolved = true;
		else IsSolved = false;
	}
	
	public Node addChild(List<Integer> data, int myindex) {
        Node child = new Node(data);
        child.parent = this;
        child.IsOrNode = !this.IsOrNode;
        this.children.add(child);
        child.index = myindex;
        return child;
    }
	
	public void setMarker(int IndexOfNode) {
		marker = IndexOfNode;
		IsMarkerSet = true;
	}
	
}
