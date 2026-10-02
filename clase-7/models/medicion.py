from datetime import datetime
from sqlalchemy import ForeignKey, Integer, String, func, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from database import Base


class Medicion(Base):
    __tablename__ = "mediciones"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    estudiante_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("estudiantes.id"), nullable=False
    )
    variable: Mapped[str] = mapped_column(String(50), nullable=False)
    valor: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    unidad: Mapped[str] = mapped_column(String(20), nullable=False)
    fecha_hora: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    estudiante = relationship("Estudiante", foreign_keys=[estudiante_id])
