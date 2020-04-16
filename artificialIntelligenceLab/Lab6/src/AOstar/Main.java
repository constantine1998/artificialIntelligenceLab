package AOstar;

import java.util.Arrays;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		List<Integer> list = GenerateTree.generateTree();
		long Futility = 10000000;
		Node Start = new Node(list);
		Start.IsOrNode = true;

		for(int i = 1; i < list.size()-1;i++) Start.addChild(list, i-1).dotPosition = i;
	    
		Start.IsMarkerSet = true;
		Start.setMarker(0);
		
		while(!Start.IsSolved && Start.hValue < Futility) {
			
			Start = ForwardPhase.forwardPhase(Start);
			
			Start = BackTracking.backTracking(Start);
			
		}
		if(Start.IsSolved) System.out.println("Tree could be solved, Optimal cost found is: "+ nodeCost.calCost(Start));
		else System.out.println("Could not find Optimal Solution. Futility Value Reached");
	}

}
