void LeftWing(Environment* pEnv, int id)
{
	Vector3D ball = pEnv->currentBall.pos;
	Vector3D opponent = pEnv->opponent[0].pos;
	Vector3D LeftWing_pos = pEnv->home[id].pos;
	Vector3D RightWing_pos = pEnv->home[2].pos;
	Vector3D Attacker_pos = pEnv->home[4].pos;
	Vector3D Goalie_pos = pEnv->home[0].pos;
	double distance = 10;
	int state = 5;
	int robotnumber = robot1(pEnv);
	// 计算左边锋与对手的距离及角度差
	double distanceToOpponent = calc_distance(LeftWing_pos.x, LeftWing_pos.y, opponent.x, opponent.y);
	double angleToOpponent = atan2(opponent.y - LeftWing_pos.y, opponent.x - LeftWing_pos.x);
	int closestOpponentId = 0;
	int closestballId = 0;
	double minDistance = 9999;
	double D = Distance(opponent.x, LeftWing_pos.x, opponent.y, LeftWing_pos.y);
	if (Distance(Goalie_pos.x, LeftWing_pos.x, Goalie_pos.y, LeftWing_pos.y) <= 10)
	{
		Position(pEnv, id, LeftWing_pos.x - 17, LeftWing_pos.y);
		stop(pEnv, 0, LeftWing_pos.x - 17, LeftWing_pos.y);
	}
    //右半场
	else if (ball.x >= 165)
	{
		if (ball.y >= 90) {
			Position(pEnv, id, 160, ball.y - 45);
		}
		else {
			Position(pEnv, id, 160, ball.y + 45);
		}
	}
	else if (ball.x >= 185)
	{
		if (ball.y <= 40) {
			Position(pEnv, id, LeftWing_pos.x + 10, max(LeftWing_pos.y + 30, 60));
		}
		else if (ball.y > 40 && ball.y < 90) {
			if (D >= 20)
			{
				Position(pEnv, id, ball.x, ball.y);
			}
			else {
				Position(pEnv, id, ball.x + 10, ball.y - 15);
				Velocity(&(pEnv->home[id]), -120, 120);
			}
		}
		else if (ball.y > 90 && ball.y < 140) {
			if (D >= 20)
			{
				Position(pEnv, id, ball.x, ball.y);
			}
			else {
				Position(pEnv, id, ball.x + 10, ball.y + 15);
				Velocity(&(pEnv->home[id]), 120, 120);
			}
		}
		else 
		{
			Position(pEnv, id, LeftWing_pos.x + 10, min(LeftWing_pos.y - 50, 80));

		}
	}
	else if (ball.x < 185 && ball.x >= 110)
	{
		if (ball.y < 90)
		{
			Position(pEnv, id, ball.x + 35, max(ball.y + 50, 55));
		}
		else
		{
			Position(pEnv, id, ball.x + 35, min(ball.y - 50, 125));
		}
	}
	else if (ball.x < 110 && ball.x > 55)
	{
		if (ball.y < 30)
		{
			Position(pEnv, id, min(LeftWing_pos.x + 35, 150), min(LeftWing_pos.y + 50, 55));
		}
		else if (ball.y > 150)
		{
			Position(pEnv, id, min(LeftWing_pos.x + 35, 150), min(LeftWing_pos.y - 50, 125));
		}
		else
		{
			if (ball.y < 90)
			{
				Position(pEnv, id, min(ball.x + 30, 150), ball.y + 30);
			}
			else
			{
				Position(pEnv, id, min(ball.x + 30, 150), ball.y - 30);
			}
		}
	}
}