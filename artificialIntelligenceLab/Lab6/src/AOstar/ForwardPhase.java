package AOstar;

public class ForwardPhase {
	
	public static Node forwardPhase(Node node) {
		while(node.IsMarkerSet) node = node.children.get(node.marker);
	
		if(node.IsOrNode) for(int i = 1; i < node.mSize-1;i++) node.addChild(node.nxm, i-1).dotPosition = i;
		else {
		
			node.addChild(node.nxm.subList(0, node.dotPosition+1), 0);
			node.addChild(node.nxm.subList(node.dotPosition, node.mSize), 1);
		}
		
		return node;
	}

}
