package hns.faker.boot.repository;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;

import hns.faker.boot.dto.ContentsVo;

public class ContentsRepositoryImpl implements ContentsRepository{
	@Autowired
	SqlSession session;

	@Override
	public int insertContents(ContentsVo contents) {
		return 0;
	}

	@Override
	public int updateContents(ContentsVo contents) {
		return 0;
	}

	@Override
	public int deleteContents(int content_id) {
		return 0;
	}

	@Override
	public ContentsVo selectContens(int content_id) {
		return null;
	}

}
